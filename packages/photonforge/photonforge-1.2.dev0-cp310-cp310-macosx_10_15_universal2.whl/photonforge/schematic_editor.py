from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, FileResponse
import photonforge as pf
import uvicorn
import asyncio
import json
import threading
import traceback
import subprocess
import os
import signal
import time
import atexit
import warnings
import logging
import sys
import io
from photonforge.live_viewer import LiveViewer
import luxtelligence_lnoi400_forge as lxt


logger = logging.getLogger(__name__)


def extract_terminals(component):
    """Extract terminal information from PhotonForge component"""
    terminal_data = []

    # Get all terminals from the component
    for terminal_name, terminal_obj in component.terminals.items():
        # Get the center of the terminal
        structure = terminal_obj.structure
        center_x, center_y = structure.center

        # Get the layer information
        layer = terminal_obj.routing_layer

        # Calculate angle based on terminal position relative to origin
        # This helps with positioning terminals on the node edges
        angle = None
        if center_x != 0 or center_y != 0:
            import math

            # Calculate angle in degrees using standard mathematical convention:
            # 0° = right (positive x-axis), 90° = up (positive y-axis),
            # 180° = left (negative x-axis), 270° = down (negative y-axis)
            # Note: atan2 takes (y, x) as arguments, not (x, y)
            angle = math.degrees(math.atan2(center_y, center_x))
            # Normalize to 0-360 range
            if angle < 0:
                angle += 360

            logger.debug(
                f"Terminal {terminal_name} at ({center_x}, {center_y}) has angle: {angle:.2f}°"
            )

        terminal_info = {
            "name": terminal_name,
            "x": float(center_x),
            "y": float(center_y),
            "layer": layer,
            "type": "Terminal",
            "angle": angle,  # Include calculated angle in the terminal data
        }
        terminal_data.append(terminal_info)

        logger.debug(
            f"Extracted terminal: {terminal_name} at position ({center_x}, {center_y}) with angle {angle}"
        )

    return terminal_data


def extract_ports(component):
    """Extract port information from PhotonForge component"""
    port_data = []
    terminal_data = []  # To collect terminals from electrical ports

    for port_name, port_obj in component.ports.items():
        center_x, center_y = port_obj.center
        angle = getattr(port_obj, "input_direction", 0)
        width = getattr(port_obj.spec, "width", None)

        # Determine if this is an electrical port
        is_electrical = False
        if hasattr(port_obj.spec, "voltage_path") and port_obj.spec.voltage_path is not None:
            is_electrical = True

        # Get string representation of port spec
        port_spec_str = str(port_obj.spec) if hasattr(port_obj, "spec") else None

        port_info = {
            "name": port_name,
            "x": float(center_x),
            "y": float(center_y),
            "angle": float(angle),
            "width": float(width) if width is not None else None,
            "type": port_obj.__class__.__name__,  # Gets the class name of the port object
            "classification": getattr(
                port_obj, "classification", None
            ),  # Gets optical/electrical classification
            "is_electrical": is_electrical,
            "spec": port_spec_str,  # Add the string representation of port spec
        }

        port_data.append(port_info)

        # Check if this electrical port has terminals
        if is_electrical and hasattr(port_obj, "terminals"):
            try:
                logger.debug(f"Found terminals in electrical port {port_name}")
                # Get terminals - handle both method and dictionary cases
                terminals = (
                    port_obj.terminals() if callable(port_obj.terminals) else port_obj.terminals
                )

                # Extract terminals from the port
                for term_name, term_obj in terminals.items():
                    # Get terminal position - use port position if terminal position not available
                    try:
                        term_center = (
                            term_obj.center if hasattr(term_obj, "center") else port_obj.center
                        )
                        term_x, term_y = term_center
                    except Exception:
                        term_x, term_y = center_x, center_y

                    # Get layer information
                    layer = term_obj.routing_layer if hasattr(term_obj, "routing_layer") else None

                    # Create a terminal info object
                    term_info = {
                        "name": f"{port_name}.{term_name}",  # Format: portName.terminalName
                        "x": float(term_x),
                        "y": float(term_y),
                        "layer": layer,
                        "type": "Terminal",
                        "angle": float(angle),  # Use port angle for now
                        "parent_port": port_name,  # Track the parent port
                    }

                    terminal_data.append(term_info)
                    logger.debug(f"Added terminal {term_info['name']} from port {port_name}")
            except Exception as e:
                logger.warning(f"Error extracting terminals from port {port_name}: {str(e)}")

    return port_data, terminal_data


def convert_to_pf_netlist(netlist, components):
    """Convert frontend netlist format to PhotonForge netlist format"""
    pf_netlist = {
        "instances": {},
        "routes": [],
        "virtual connections": [],
        "connections": [],
        "ports": [],
        "terminal routes": [],
        "terminals": [],  # Add terminals key to the netlist
    }

    # Process instances
    for key, instance in netlist["instances"].items():
        component_name = instance["component"]
        origin = instance["origin"]
        rotation = instance["rotation"]

        # Parse origin from string format "(x, y)" to tuple
        if isinstance(origin, str):
            origin_parts = origin.strip("()").split(",")
            origin_tuple = (float(origin_parts[0]), float(origin_parts[1]))
        else:
            origin_tuple = tuple(origin)

        pf_netlist["instances"][key] = {
            "component": components[component_name],
            "origin": origin_tuple,
            "rotation": rotation,
        }

    # Process routes
    for route in netlist["routes"]:
        # print(f"\nProcessing route: {route}")  # Debug print

        # Parse port tuples from string format "(key, port)" to actual tuples
        source = route[0].strip("()").split(",") if isinstance(route[0], str) else route[0]
        target = route[1].strip("()").split(",") if isinstance(route[1], str) else route[1]

        source_tuple = (source[0].strip(), source[1].strip())
        target_tuple = (target[0].strip(), target[1].strip())

        # Check if there's additional route data
        if len(route) > 2:
            route_data = route[2]
            # print(f"Route data: {route_data}")  # Debug print

            # Process route style first
            if "style" in route_data:
                style = route_data["style"]
                # print(f"Route style: {style}")  # Debug print

                if style == "sbend":
                    # For S-bend routes
                    route_entry = [source_tuple, target_tuple, pf.parametric.route_s_bend]
                    # Add euler_fraction if specified
                    if "eulerFraction" in route_data:
                        euler_fraction = float(route_data["eulerFraction"])
                        route_entry.append({"euler_fraction": euler_fraction})
                        # print(f"Adding S-bend route with euler_fraction: {euler_fraction}")  # Debug print
                    pf_netlist["routes"].append(route_entry)
                else:
                    # For Manhattan routes
                    route_kwargs = {}
                    # Process waypoints
                    if "waypoints" in route_data:
                        waypoints = []
                        for waypoint in route_data["waypoints"]:
                            if isinstance(waypoint, str):
                                wp_parts = waypoint.strip("()").split(",")
                                waypoints.append((float(wp_parts[0]), float(wp_parts[1])))
                            else:
                                waypoints.append(tuple(waypoint))
                        route_kwargs["waypoints"] = waypoints

                    # Process bend radius
                    if "radius" in route_data:
                        route_kwargs["radius"] = float(route_data["radius"])

                    # print(f"Adding Manhattan route with kwargs: {route_kwargs}")  # Debug print
                    pf_netlist["routes"].append([source_tuple, target_tuple, route_kwargs])
            else:
                # Default Manhattan route
                route_kwargs = {}
                if "waypoints" in route_data:
                    waypoints = []
                    for waypoint in route_data["waypoints"]:
                        if isinstance(waypoint, str):
                            wp_parts = waypoint.strip("()").split(",")
                            waypoints.append((float(wp_parts[0]), float(wp_parts[1])))
                        else:
                            waypoints.append(tuple(waypoint))
                    route_kwargs["waypoints"] = waypoints

                if "radius" in route_data:
                    route_kwargs["radius"] = float(route_data["radius"])

                # print(f"Adding default Manhattan route with kwargs: {route_kwargs}")  # Debug print
                pf_netlist["routes"].append([source_tuple, target_tuple, route_kwargs])
        else:
            # print("Adding simple route without parameters")  # Debug print
            pf_netlist["routes"].append([source_tuple, target_tuple])

    # Process connections
    for connection in netlist["connections"]:
        # Parse port tuples from string format "(key, port)" to actual tuples
        source = (
            connection[0].strip("()").split(",")
            if isinstance(connection[0], str)
            else connection[0]
        )
        target = (
            connection[1].strip("()").split(",")
            if isinstance(connection[1], str)
            else connection[1]
        )

        source_tuple = (source[0].strip(), source[1].strip())
        target_tuple = (target[0].strip(), target[1].strip())

        pf_netlist["connections"].append([source_tuple, target_tuple])

    # Process virtual connections
    if "virtual" in netlist:
        for virtual_conn in netlist["virtual"]:
            # Parse port tuples from string format "(key, port)" to actual tuples
            source = (
                virtual_conn[0].strip("()").split(",")
                if isinstance(virtual_conn[0], str)
                else virtual_conn[0]
            )
            target = (
                virtual_conn[1].strip("()").split(",")
                if isinstance(virtual_conn[1], str)
                else virtual_conn[1]
            )

            source_tuple = (source[0].strip(), source[1].strip())
            target_tuple = (target[0].strip(), target[1].strip())

            pf_netlist["virtual connections"].append([source_tuple, target_tuple])

    # Process ports
    for port in netlist["ports"]:
        if isinstance(port, str):
            # Parse port tuple from string format "(key, port)" to actual tuple
            port_parts = port.strip("()").split(",")
            port_tuple = (port_parts[0].strip(), port_parts[1].strip())
        else:
            port_tuple = tuple(port)
        pf_netlist["ports"].append(port_tuple)

    # Process terminal routes
    if "terminal_routes" in netlist and netlist["terminal_routes"]:
        for terminal_route in netlist["terminal_routes"]:
            try:
                # Parse terminal tuples
                if isinstance(terminal_route[0], str):
                    source_str = terminal_route[0].strip("()").split(",")
                    source_id = source_str[0].strip()
                    source_terminal = source_str[1].strip() if len(source_str) > 1 else ""
                else:
                    source_id = (
                        terminal_route[0][0]
                        if isinstance(terminal_route[0], list)
                        else terminal_route[0]
                    )
                    source_terminal = (
                        terminal_route[0][1] if isinstance(terminal_route[0], list) else ""
                    )

                if isinstance(terminal_route[1], str):
                    target_str = terminal_route[1].strip("()").split(",")
                    target_id = target_str[0].strip()
                    target_terminal = target_str[1].strip() if len(target_str) > 1 else ""
                else:
                    target_id = (
                        terminal_route[1][0]
                        if isinstance(terminal_route[1], list)
                        else terminal_route[1]
                    )
                    target_terminal = (
                        terminal_route[1][1] if isinstance(terminal_route[1], list) else ""
                    )

                # Create the terminal route entry
                terminal_route_entry = [(source_id, source_terminal), (target_id, target_terminal)]

                # Add route data if it exists
                if len(terminal_route) > 2:
                    route_data = terminal_route[2]
                    route_kwargs = {}

                    # Process waypoints for terminal routes - convert to flat list
                    if "waypoints" in route_data:
                        flat_waypoints = []
                        for waypoint in route_data["waypoints"]:
                            if isinstance(waypoint, str):
                                wp_parts = waypoint.strip("()").split(",")
                                flat_waypoints.extend([float(wp_parts[0]), float(wp_parts[1])])
                            else:
                                flat_waypoints.extend([float(waypoint[0]), float(waypoint[1])])
                        route_kwargs["waypoints"] = flat_waypoints

                    # Process bend radius
                    if "radius" in route_data:
                        route_kwargs["radius"] = float(route_data["radius"])

                    # Process terminal route parameters
                    # Width of the routing path
                    if "width" in route_data:
                        route_kwargs["width"] = float(route_data["width"])

                    # Direction of the route at the first terminal
                    if "direction1" in route_data:
                        # Only add if not empty string
                        if route_data["direction1"]:
                            route_kwargs["direction1"] = route_data["direction1"]

                    # Direction of the route at the second terminal
                    if "direction2" in route_data:
                        # Only add if not empty string
                        if route_data["direction2"]:
                            route_kwargs["direction2"] = route_data["direction2"]

                    # Add kwargs if we have any
                    if route_kwargs:
                        terminal_route_entry.append(route_kwargs)

                pf_netlist["terminal routes"].append(terminal_route_entry)

            except Exception as e:
                print(f"Error processing terminal route: {e}")
                import traceback

                traceback.print_exc()
                continue

    # Process terminals
    if "terminals" in netlist and netlist["terminals"]:
        for terminal in netlist["terminals"]:
            try:
                # Parse terminal tuple
                if isinstance(terminal, str):
                    terminal_str = terminal.strip("()").split(",")
                    instance_id = terminal_str[0].strip()

                    # Check if this is a terminal in a port (portName, terminalName)
                    if "(" in terminal_str[1] and ")" in terminal_str[1]:
                        # This is a terminal within a port
                        port_terminal_str = terminal_str[1].strip().strip("()").split(",")
                        port_name = port_terminal_str[0].strip()
                        terminal_name = port_terminal_str[1].strip()
                        terminal_tuple = (instance_id, (port_name, terminal_name))
                    else:
                        # Regular terminal
                        terminal_name = terminal_str[1].strip()
                        terminal_tuple = (instance_id, terminal_name)
                else:
                    instance_id = terminal[0]

                    # Check if this is a terminal in a port
                    if isinstance(terminal[1], (list, tuple)) and len(terminal[1]) == 2:
                        port_name = terminal[1][0]
                        terminal_name = terminal[1][1]
                        terminal_tuple = (instance_id, (port_name, terminal_name))
                    else:
                        terminal_name = terminal[1]
                        terminal_tuple = (instance_id, terminal_name)

                pf_netlist["terminals"].append(terminal_tuple)

            except Exception as e:
                print(f"Error processing terminal: {e}")
                import traceback

                traceback.print_exc()
                continue

    # print("\nFinal netlist routes:")  # Debug print
    # for route in pf_netlist["routes"]:
    #    print(route)

    return pf_netlist


def create_bond_pad(size=100, type="Circle"):
    """Create a bond pad component"""
    component = pf.Component("Bond pad")
    # Add the metal rectangle for the pad
    if type == "Circle":
        component.add("METAL", pf.Circle(center=(0, 0), radius=size / 2))
        pad_terminal = pf.Terminal("METAL", pf.Circle(center=(0, 0), radius=size / 2 - 5))
    elif type == "Rectangle":
        component.add("METAL", pf.Rectangle(center=(0, 0), size=(size, size)))
        pad_terminal = pf.Terminal("METAL", pf.Rectangle(center=(0, 0), size=(size - 5, size - 5)))
    # Add the terminal to the component
    component.add_terminal(pad_terminal)

    return component


def translate_component(comp, translate=(0, 0)):
    """
    Create a new component by translating an existing component.

    Args:
        comp: The original component to translate
        translate: Tuple (dx, dy) with the translation values

    Returns:
        A new component with all elements translated
    """
    # Create a new component with the same name
    c = pf.Component(name=comp.name)

    # Add a reference to the original component with translation
    ref = pf.Reference(comp)
    ref.translate(translate)
    c.add(ref)

    # Process all ports from the reference
    for port_name, port_info in ref.get_ports().items():
        port = port_info[0]  # The actual port object
        c.add_port(port, port_name)

    # Process all terminals from the reference
    for terminal_name, terminal_info in ref.get_terminals().items():
        terminal = terminal_info[0]  # The actual terminal object
        c.add_terminal(terminal, terminal_name)

    # Copy over any models from the original component
    if hasattr(comp, "models") and comp.models:
        for model in comp.models:
            c.add_model(model)

    logger.info(f"Original component bounds: {comp.bounds()}")
    logger.info(f"Translated component bounds: {c.bounds()}")

    return c


def generate_python_code(netlist, components):
    """Generate Python code that reproduces the netlist"""
    code_lines = []

    # Add imports
    code_lines.append("import photonforge as pf")
    code_lines.append("import photonforge.parametric as param")
    code_lines.append("")

    # Track components used
    component_names = set()
    for instance in netlist["instances"].values():
        component_names.add(instance["component"])

    # Add code for loading components - Option 2 (using PHF) is now the default
    code_lines.append("# Load components from the PHF file")
    code_lines.append("loaded = pf.load_phf('circuit_components.phf')")
    code_lines.append("components = {}")
    code_lines.append("for comp in loaded['components']:")
    code_lines.append("    # Map component by its name")
    code_lines.append("    components[comp.name] = comp")
    code_lines.append("")

    # Create component instances
    code_lines.append("# Component instances")
    for instance_id, instance in netlist["instances"].items():
        component_name = instance["component"]
        origin = instance["origin"]
        rotation = instance["rotation"]

        var_name = f"{instance_id.replace('-', '_')}"
        code_lines.append(f"{var_name} = {{")
        code_lines.append(
            f"    'component': components['{component_name}'],  # Reference to component by name"
        )
        code_lines.append(f"    'origin': {origin},")
        code_lines.append(f"    'rotation': {rotation}")
        code_lines.append("}")
        code_lines.append("")

    # Create routes section with all parameters
    if "routes" in netlist and netlist["routes"]:
        code_lines.append("# Routes with parameters")
        code_lines.append("routes = [")
        for route in netlist["routes"]:
            source = route[0]
            target = route[1]

            # Format source and target as string tuples
            source_parts = source.strip("()").split(",") if isinstance(source, str) else source
            target_parts = target.strip("()").split(",") if isinstance(target, str) else target

            source_instance = (
                source_parts[0].strip() if isinstance(source_parts, list) else source_parts[0]
            )
            source_port = (
                source_parts[1].strip() if isinstance(source_parts, list) else source_parts[1]
            )

            target_instance = (
                target_parts[0].strip() if isinstance(target_parts, list) else target_parts[0]
            )
            target_port = (
                target_parts[1].strip() if isinstance(target_parts, list) else target_parts[1]
            )

            if len(route) > 2:
                # This route has parameters
                params = route[2]
                route_line = f'    [("{source_instance}", "{source_port}"), ("{target_instance}", "{target_port}")'

                if isinstance(params, dict) and "style" in params:
                    if params["style"] == "sbend":
                        route_line += ", param.route_s_bend"
                        if "eulerFraction" in params:
                            route_line += f", {{'euler_fraction': {params['eulerFraction']}}}"
                    else:
                        route_line += ", {"
                        if "waypoints" in params:
                            waypoints = params["waypoints"]
                            route_line += f"\n        'waypoints': {waypoints},"
                        if "radius" in params:
                            route_line += f"\n        'radius': {params['radius']},"
                        route_line += "\n    }"
                code_lines.append(route_line + "],")
            else:
                # Simple route without parameters
                code_lines.append(
                    f'    [("{source_instance}", "{source_port}"), ("{target_instance}", "{target_port}")],'
                )
        code_lines.append("]")
        code_lines.append("")

    # Create connections section
    if "connections" in netlist and netlist["connections"]:
        code_lines.append("# Direct connections")
        code_lines.append("connections = [")
        for conn in netlist["connections"]:
            source = conn[0]
            target = conn[1]

            # Format source and target as string tuples
            source_parts = source.strip("()").split(",") if isinstance(source, str) else source
            target_parts = target.strip("()").split(",") if isinstance(target, str) else target

            source_instance = (
                source_parts[0].strip() if isinstance(source_parts, list) else source_parts[0]
            )
            source_port = (
                source_parts[1].strip() if isinstance(source_parts, list) else source_parts[1]
            )

            target_instance = (
                target_parts[0].strip() if isinstance(target_parts, list) else target_parts[0]
            )
            target_port = (
                target_parts[1].strip() if isinstance(target_parts, list) else target_parts[1]
            )

            code_lines.append(
                f'    [("{source_instance}", "{source_port}"), ("{target_instance}", "{target_port}")],'
            )
        code_lines.append("]")
        code_lines.append("")

    # Create virtual connections section
    if "virtual" in netlist and netlist["virtual"]:
        code_lines.append("# Virtual connections")
        code_lines.append("virtual_connections = [")
        for conn in netlist["virtual"]:
            source = conn[0]
            target = conn[1]

            # Format source and target as string tuples
            source_parts = source.strip("()").split(",") if isinstance(source, str) else source
            target_parts = target.strip("()").split(",") if isinstance(target, str) else target

            source_instance = (
                source_parts[0].strip() if isinstance(source_parts, list) else source_parts[0]
            )
            source_port = (
                source_parts[1].strip() if isinstance(source_parts, list) else source_parts[1]
            )

            target_instance = (
                target_parts[0].strip() if isinstance(target_parts, list) else target_parts[0]
            )
            target_port = (
                target_parts[1].strip() if isinstance(target_parts, list) else target_parts[1]
            )

            code_lines.append(
                f'    [("{source_instance}", "{source_port}"), ("{target_instance}", "{target_port}")],'
            )
        code_lines.append("]")
        code_lines.append("")

    # Create ports section
    if "ports" in netlist and netlist["ports"]:
        code_lines.append("# Exposed ports")
        code_lines.append("ports = [")
        for port in netlist["ports"]:
            # Format port as string tuple
            if isinstance(port, str):
                port_parts = port.strip("()").split(",")
                instance = port_parts[0].strip()
                port_name = port_parts[1].strip()
            else:
                instance = port[0]
                port_name = port[1]

            code_lines.append(f'    ("{instance}", "{port_name}"),')
        code_lines.append("]")
        code_lines.append("")

    # Terminal routes
    if "terminal_routes" in netlist and netlist["terminal_routes"]:
        code_lines.append("# Terminal routes")
        code_lines.append("terminal_routes = [")
        for route in netlist["terminal_routes"]:
            source = route[0]
            target = route[1]

            # Format source and target as string tuples
            source_parts = source.strip("()").split(",") if isinstance(source, str) else source
            target_parts = target.strip("()").split(",") if isinstance(target, str) else target

            source_instance = (
                source_parts[0].strip() if isinstance(source_parts, list) else source_parts[0]
            )
            source_terminal = (
                source_parts[1].strip()
                if isinstance(source_parts, list) and len(source_parts) > 1
                else ""
            )

            target_instance = (
                target_parts[0].strip() if isinstance(target_parts, list) else target_parts[0]
            )
            target_terminal = (
                target_parts[1].strip()
                if isinstance(target_parts, list) and len(target_parts) > 1
                else ""
            )

            if len(route) > 2:
                # This route has parameters
                params = route[2]
                route_line = f'    [("{source_instance}", "{source_terminal}"), ("{target_instance}", "{target_terminal}")'

                if isinstance(params, dict):
                    route_line += ", {"
                    for key, value in params.items():
                        if key == "waypoints":
                            route_line += f"\n        '{key}': {value},"
                        else:
                            route_line += f"\n        '{key}': {value},"
                    route_line += "\n    }"
                code_lines.append(route_line + "],")
            else:
                code_lines.append(
                    f'    [("{source_instance}", "{source_terminal}"), ("{target_instance}", "{target_terminal}")],'
                )
        code_lines.append("]")
        code_lines.append("")

    # Terminals
    if "terminals" in netlist and netlist["terminals"]:
        code_lines.append("# Terminals")
        code_lines.append("terminals = [")
        for terminal in netlist["terminals"]:
            # Format terminal as string tuple
            if isinstance(terminal, str):
                terminal_parts = terminal.strip("()").split(",")
                instance = terminal_parts[0].strip()
                terminal_name = terminal_parts[1].strip()
            else:
                instance = terminal[0]
                terminal_name = terminal[1]

            code_lines.append(f'    ("{instance}", "{terminal_name}"),')
        code_lines.append("]")
        code_lines.append("")

    # Build the final netlist
    code_lines.append("# Create the complete netlist")
    code_lines.append("netlist = {")
    code_lines.append("    'name': 'generated_from_gui',")

    # Instances
    code_lines.append("    'instances': {")
    for instance_id in netlist["instances"]:
        var_name = instance_id.replace("-", "_")
        code_lines.append(f"        '{instance_id}': {var_name},")
    code_lines.append("    },")

    # Add other netlist components
    if "routes" in netlist and netlist["routes"]:
        code_lines.append("    'routes': routes,")
    if "connections" in netlist and netlist["connections"]:
        code_lines.append("    'connections': connections,")
    if "ports" in netlist and netlist["ports"]:
        code_lines.append("    'ports': ports,")
    if "virtual" in netlist and netlist["virtual"]:
        code_lines.append("    'virtual connections': virtual_connections,")
    if "terminal_routes" in netlist and netlist["terminal_routes"]:
        code_lines.append("    'terminal routes': terminal_routes,")
    if "terminals" in netlist and netlist["terminals"]:
        code_lines.append("    'terminals': terminals,")

    code_lines.append("}")
    code_lines.append("")

    # Generate the component and display
    code_lines.append("# Create the component")
    code_lines.append("comp = pf.component_from_netlist(netlist)")
    code_lines.append("comp")

    return "\n".join(code_lines)


def create_component_phf(netlist, components, output_path="circuit_components.phf"):
    """
    Create a PHF file with all components needed for the netlist.
    Copies and renames components to match their dictionary keys for easier loading.

    Args:
        netlist: The netlist containing component references
        components: Dictionary of components (editor.components)
        output_path: Path where the PHF file should be saved

    Returns:
        Path to the saved PHF file
    """
    import os

    # Get unique component names used in this netlist
    component_names = set()
    for instance in netlist["instances"].values():
        component_names.add(instance["component"])

    # Create copies of components with names matching their dictionary keys
    renamed_components = []
    for comp_key in component_names:
        if comp_key in components:
            # Get the original component
            orig_comp = components[comp_key]

            # Skip if the name already matches the key
            if orig_comp.name == comp_key:
                renamed_components.append(orig_comp)
                continue

            # Create a copy with the key as the name
            logger.info(f"Creating copy of component '{orig_comp.name}' with new name '{comp_key}'")
            copy_comp = pf.Component(comp_key)

            # Add a reference to the original component
            ref = pf.Reference(orig_comp)
            copy_comp.add(ref)

            # Process all ports from the reference
            for port_name, port_info in ref.get_ports().items():
                port = port_info[0]  # The actual port object
                copy_comp.add_port(port, port_name)

            # Process all terminals from the reference
            for terminal_name, terminal_info in ref.get_terminals().items():
                terminal = terminal_info[0]  # The actual terminal object
                copy_comp.add_terminal(terminal, terminal_name)

            # Copy over any models from the original component
            if hasattr(orig_comp, "models") and orig_comp.models:
                for name, model in orig_comp.models.items():
                    copy_comp.add_model(model, name)

            # If orig_comp has a technology attribute, copy it
            if hasattr(orig_comp, "technology") and orig_comp.technology:
                copy_comp.technology = orig_comp.technology

            renamed_components.append(copy_comp)
        else:
            logger.warning(f"Component '{comp_key}' not found in components dictionary")

    # Save components to PHF file
    if renamed_components:
        # Create directory for the output file if it doesn't exist
        dir_path = os.path.dirname(output_path)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

        # Save the components
        pf.write_phf(output_path, *renamed_components)
        logger.info(f"Saved {len(renamed_components)} components to {output_path}")
        return output_path
    else:
        logger.warning("No components to save")
        return None


# Custom warning handler to capture warnings
class WarningCatcher:
    def __init__(self):
        self.warnings = []
        self.max_warnings = 50  # Maximum number of warnings to store

    def __call__(self, message, category, filename, lineno, file=None, line=None):
        warning_msg = f"{category.__name__}: {message} (in {filename}:{lineno})"

        # Truncate extremely long warning messages
        if len(warning_msg) > 1000:
            warning_msg = warning_msg[:1000] + "... (truncated)"

        # Only store if not a duplicate
        if warning_msg not in self.warnings:
            self.warnings.append(warning_msg)
            # Limit the number of warnings stored
            if len(self.warnings) > self.max_warnings:
                self.warnings = self.warnings[-self.max_warnings :]
            print(f"WARNING: {warning_msg}")

        # Don't call the default handler to avoid recursion
        # Just write to stderr directly instead
        if file is None:
            file = sys.stderr
        try:
            file.write(warnings.formatwarning(message, category, filename, lineno, line))
        except Exception:
            # If writing fails, just ignore it - don't cause more problems
            pass


class SchematicEditor:
    """
    SchematicEditor class that manages the backend server and provides methods
    to add/remove components programmatically.
    """

    def __init__(
        self, port=8000, frontend_port=3000, start=True, start_frontend=True, reset_canvas=True
    ):
        # Initialize FastAPI app
        self.app = FastAPI()
        self.port = port
        self.frontend_port = frontend_port
        self.server = None
        self.server_thread = None
        self.frontend_process = None
        self.components = {}
        self.clients = {}  # Dictionary to store client queues

        # Error and warning collection
        self.errors = []
        self.warnings = []
        self.max_log_size = 50  # Maximum number of errors/warnings to keep

        # Set up custom warning handler
        self.warning_handler = WarningCatcher()
        warnings.showwarning = self.warning_handler

        # Initialize live viewer with output suppressed
        original_stdout = sys.stdout
        sys.stdout = io.StringIO()  # Redirect stdout to suppress LiveViewer message
        self.viewer = LiveViewer()
        sys.stdout = original_stdout  # Restore stdout

        self.latest_components = None  # Cache for the latest components data
        self.reset_canvas = reset_canvas  # Whether to reset canvas on startup

        # Enable CORS
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        # Initialize Luxtelligence technology
        self.tech = lxt.lnoi400()
        pf.config.default_technology = self.tech
        pf.config.default_radius = 5

        # Set up routes
        self._setup_routes()

        # Initialize with Luxtelligence components
        self._initialize_default_components()

        # Start servers if requested
        if start:
            self.start()

        if start_frontend:
            self.start_frontend()

        # Register cleanup function to stop servers on exit
        atexit.register(self.cleanup)

        # Create exports directory if it doesn't exist
        os.makedirs("./exports", exist_ok=True)

        @self.app.get("/download_phf/{filename}")
        async def download_phf(filename: str):
            """Download a PHF file"""
            # Ensure the file exists
            file_path = os.path.join("./exports", filename)
            if not os.path.exists(file_path):
                return {"error": "File not found"}, 404

            return FileResponse(
                path=file_path, filename=filename, media_type="application/octet-stream"
            )

    def _setup_routes(self):
        """Set up the FastAPI routes"""

        @self.app.get("/components")
        async def get_components():
            """Return list of available components with their properties"""
            return self._get_components_info()

        @self.app.get("/clear_canvas")
        async def clear_canvas():
            """Endpoint to clear the canvas data in the frontend"""
            should_clear = self.reset_canvas
            # Reset the flag after the first check
            self.reset_canvas = False
            return {
                "status": "success",
                "should_clear": should_clear,
                "message": "Request to clear canvas processed",
            }

        @self.app.post("/generate_layout")
        async def generate_layout(netlist: dict):
            return await self._generate_layout(netlist)

        @self.app.post("/save_component")
        async def save_component(data: dict):
            return await self._save_component(data)

        @self.app.delete("/delete_component")
        async def delete_component(data: dict):
            return await self._delete_component(data)

        @self.app.post("/export_python_code")
        async def export_python_code(netlist: dict):
            """Generate a Python script and component PHF file from the current netlist"""
            try:
                # Generate timestamp to use in filenames
                from datetime import datetime

                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

                python_code = generate_python_code(netlist, self.components)

                # Create a .phf file with the required components
                phf_filename = f"circuit_components_{timestamp}.phf"
                phf_path = create_component_phf(
                    netlist, self.components, f"./exports/{phf_filename}"
                )

                # Update the Python code to point to the correct PHF file
                python_code = python_code.replace("circuit_components.phf", phf_filename)

                return {"code": python_code, "phf_file": phf_filename if phf_path else None}
            except Exception as e:
                self.log_error(f"Error generating Python code: {str(e)}")
                traceback.print_exc()
                return {"error": str(e)}, 500

        @self.app.get("/errors")
        async def get_errors():
            """Return recent errors and warnings"""
            # Include warnings from warning handler (with limits)
            warnings_list = self.warnings.copy()[-50:]  # Limit to most recent 50

            # Also add warnings from warning handler if any
            if self.warning_handler.warnings:
                for warning in self.warning_handler.warnings:
                    # Truncate warning messages that are too long to prevent recursion
                    if len(warning) > 1000:
                        warning = warning[:1000] + "... (truncated)"

                    if warning not in warnings_list:
                        warnings_list.append(warning)

                # Reset the warning handler's list after retrieving them
                self.warning_handler.warnings = []

                # Keep the list size reasonable
                warnings_list = warnings_list[-50:]  # Keep only the most recent 50

            # Also limit errors
            errors_list = self.errors.copy()[-50:]  # Limit to most recent 50

            return {
                "errors": errors_list,
                "warnings": warnings_list,
            }

        @self.app.post("/clear_errors")
        async def clear_errors():
            """Clear all errors and warnings in the backend"""
            self.errors = []
            self.warnings = []
            self.warning_handler.warnings = []
            return {"message": "All errors and warnings cleared"}

        @self.app.get("/sse")
        async def sse(request: Request):
            """SSE endpoint for real-time updates"""
            client_id = id(request)
            queue = asyncio.Queue()
            self.clients[client_id] = queue

            # Immediately send the current components data
            components_info = self._get_components_info()
            await queue.put(components_info)

            async def event_generator():
                try:
                    while True:
                        if await request.is_disconnected():
                            break

                        try:
                            # Wait for new data with a timeout
                            data = await asyncio.wait_for(queue.get(), timeout=5.0)
                            yield f"data: {json.dumps(data)}\n\n"
                        except asyncio.TimeoutError:
                            # Send a heartbeat with the latest data
                            yield f"data: {json.dumps(self._get_components_info())}\n\n"
                except Exception:
                    traceback.print_exc()
                finally:
                    # Clean up when the client disconnects
                    if client_id in self.clients:
                        del self.clients[client_id]

            return StreamingResponse(event_generator(), media_type="text/event-stream")

    def log_error(self, message):
        """Add an error message to the error log"""
        if message not in self.errors:  # Prevent duplicates
            self.errors.insert(0, message)
            self.errors = self.errors[: self.max_log_size]
            print(f"ERROR: {message}")

    def log_warning(self, message):
        """Add a warning message to the warning log"""
        # Truncate extremely long messages
        if len(message) > 1000:
            message = message[:1000] + "... (truncated)"

        if message not in self.warnings:  # Prevent duplicates
            self.warnings.insert(0, message)
            self.warnings = self.warnings[: self.max_log_size]
            print(f"WARNING: {message}")

    def _get_components_info(self):
        """Get information about all components"""
        components_info = []

        for name, component in self.components.items():
            try:
                # Extract SVG representation
                svg = component._repr_svg_()

                # Extract ports and terminals
                ports_and_terminals = extract_ports(component)
                if isinstance(ports_and_terminals, tuple) and len(ports_and_terminals) == 2:
                    # New format: (port_data, terminal_data)
                    ports = ports_and_terminals[0]
                    port_terminals = ports_and_terminals[1]
                else:
                    # Legacy format: just port_data
                    ports = ports_and_terminals
                    port_terminals = []

                # Get component's own terminals
                terminals = extract_terminals(component)

                # Combine component's terminals with port terminals
                all_terminals = terminals + port_terminals

                # Determine if this is a user-created component
                is_user_created = name not in [
                    "chip_frame",
                    "cpw_probe_pad_linear",
                    "dir_coupl",
                    "double_linear_inverse_taper",
                    "eo_phase_shifter",
                    "heated_straight_waveguide",
                    "heater_pad",
                    "heater_straight",
                    "l_turn_bend",
                    "mmi1x2",
                    "mmi2x2",
                    "mz_modulator_unbalanced",
                    "s_bend_var_width",
                    "s_bend_vert",
                    "u_bend_racetrack",
                    "u_turn_bend",
                ]

                # Add component info to the list
                components_info.append(
                    {
                        "name": name,
                        "svg": svg,
                        "ports": ports,
                        "terminals": all_terminals,
                        "isUserCreated": is_user_created,
                    }
                )
            except Exception:
                error_msg = f"Error extracting component info for {name}"
                self.log_error(error_msg)
                traceback.print_exc()

        # Cache the latest components data
        self.latest_components = components_info
        return components_info

    def _initialize_default_components(self):
        """Initialize Luxtelligence components"""
        # Create Luxtelligence components
        chip_frame = lxt.component.chip_frame()
        cpw_probe_pad_linear = lxt.component.cpw_probe_pad_linear()
        dir_coupl = lxt.component.dir_coupl()
        double_linear_inverse_taper = lxt.component.double_linear_inverse_taper()
        eo_phase_shifter = lxt.component.eo_phase_shifter()
        heated_straight_waveguide = lxt.component.heated_straight_waveguide()
        heater_pad = lxt.component.heater_pad()
        heater_straight = lxt.component.heater_straight()
        l_turn_bend = lxt.component.l_turn_bend()
        mmi1x2 = lxt.component.mmi1x2()
        mmi2x2 = lxt.component.mmi2x2()
        mz_modulator_unbalanced = lxt.component.mz_modulator_unbalanced()
        s_bend_var_width = lxt.component.s_bend_var_width()
        s_bend_vert = lxt.component.s_bend_vert()
        u_bend_racetrack = lxt.component.u_bend_racetrack()
        u_turn_bend = lxt.component.u_turn_bend()

        # Add components to the dictionary
        self.components = {
            "chip_frame": chip_frame,
            "cpw_probe_pad_linear": cpw_probe_pad_linear,
            "dir_coupl": dir_coupl,
            "double_linear_inverse_taper": double_linear_inverse_taper,
            "eo_phase_shifter": eo_phase_shifter,
            "heated_straight_waveguide": heated_straight_waveguide,
            "heater_pad": heater_pad,
            "heater_straight": heater_straight,
            "l_turn_bend": l_turn_bend,
            "mmi1x2": mmi1x2,
            "mmi2x2": mmi2x2,
            "mz_modulator_unbalanced": mz_modulator_unbalanced,
            "s_bend_var_width": s_bend_var_width,
            "s_bend_vert": s_bend_vert,
            "u_bend_racetrack": u_bend_racetrack,
            "u_turn_bend": u_turn_bend,
        }

    async def _generate_layout(self, netlist):
        """Generate layout from netlist"""
        # Store the original warning filter and handler
        original_warning_filter = warnings.filters.copy() if hasattr(warnings, "filters") else []
        original_showwarning = warnings.showwarning

        try:
            # Clear existing warnings before generating layout
            self.warning_handler.warnings = []

            # Temporarily modify warning behavior for critical operations
            # This prevents warnings from triggering our custom handler during component generation
            warnings.filterwarnings("ignore", category=RuntimeWarning)
            warnings.showwarning = lambda *args, **kwargs: None

            # Convert to PhotonForge netlist format
            pf_netlist = convert_to_pf_netlist(netlist, self.components)

            # Check if we need to update technology based on components in the netlist
            # Look at the first component in instances to determine the technology
            if "instances" in netlist and netlist["instances"]:
                first_instance = list(netlist["instances"].values())[0]
                component_name = first_instance.get("component")

                if component_name and component_name in self.components:
                    component = self.components[component_name]
                    if hasattr(component, "technology") and component.technology:
                        # self.log_info(f"Updating technology to match component '{component_name}'")
                        # Store original technology
                        original_tech = pf.config.default_technology
                        # Update to component's technology
                        pf.config.default_technology = component.technology

            # Generate the component using PhotonForge
            component = pf.component_from_netlist(pf_netlist)

            # Reset technology to original if needed
            if "instances" in netlist and netlist["instances"] and "original_tech" in locals():
                pf.config.default_technology = original_tech

            # Display in live viewer
            self.viewer.display(component)

            # Restore original warning behavior
            warnings.filters = original_warning_filter
            warnings.showwarning = original_showwarning

            # Now it's safe to process warnings without risking recursion
            # Just log the first few warnings to avoid overloading the message system
            if self.warning_handler.warnings:
                max_warnings_to_show = 5  # Limit number of warnings we display
                for i, warning in enumerate(self.warning_handler.warnings[:max_warnings_to_show]):
                    # Truncate warning messages that are too long
                    if len(warning) > 1000:
                        warning = warning[:1000] + "... (truncated)"
                    self.log_warning(warning)

                if len(self.warning_handler.warnings) > max_warnings_to_show:
                    self.log_warning(
                        f"... and {len(self.warning_handler.warnings) - max_warnings_to_show} more warnings (suppressed)"
                    )

                # Clear warnings after processing
                self.warning_handler.warnings = []

            return {"message": "Layout generated successfully"}
        except Exception as e:
            # Restore original warning behavior even if there's an error
            warnings.filters = original_warning_filter
            warnings.showwarning = original_showwarning

            error_msg = f"Layout generation error: {str(e)}"
            self.log_error(error_msg)
            traceback.print_exc()
            # Ensure we only return a string representation of the error
            return {"error": str(e)[:1000]}, 500

    async def _save_component(self, data):
        """Save a component from netlist"""
        # Store the original warning filter and handler
        original_warning_filter = warnings.filters.copy() if hasattr(warnings, "filters") else []
        original_showwarning = warnings.showwarning

        try:
            component_name = data.get("name")
            netlist = data.get("netlist")

            if not component_name or not netlist:
                error_msg = "Component name and netlist are required"
                self.log_error(error_msg)
                return {"error": error_msg}, 400

            # Clear existing warnings before generating component
            self.warning_handler.warnings = []

            # Temporarily modify warning behavior for critical operations
            warnings.filterwarnings("ignore", category=RuntimeWarning)
            warnings.showwarning = lambda *args, **kwargs: None

            # Check if we need to update technology based on components in the netlist
            # Look at the first component in instances to determine the technology
            original_tech = None
            if "instances" in netlist and netlist["instances"]:
                first_instance = list(netlist["instances"].values())[0]
                component_name_in_netlist = first_instance.get("component")

                if component_name_in_netlist and component_name_in_netlist in self.components:
                    component = self.components[component_name_in_netlist]
                    if hasattr(component, "technology") and component.technology:
                        # self.log_warning(f"Updating technology to match component '{component_name_in_netlist}'")
                        # Store original technology
                        original_tech = pf.config.default_technology
                        # Update to component's technology
                        pf.config.default_technology = component.technology

            # Convert to PhotonForge netlist format using the helper function
            pf_netlist = convert_to_pf_netlist(netlist, self.components)

            # Generate the component using PhotonForge
            new_component = pf.component_from_netlist(pf_netlist)

            # Translate component so that the origin is at the bottom left corner
            bounds = new_component.bounds()
            new_component.name = component_name

            # Calculate translation needed to move center to origin
            bounds_width = bounds[1][0] - bounds[0][0]
            bounds_height = bounds[1][1] - bounds[0][1]
            center_x = bounds[0][0] + bounds_width / 2
            center_y = bounds[0][1] + bounds_height / 2
            translation = (-center_x, -center_y)

            # Create translated component
            new_component_translated = translate_component(new_component, translate=translation)

            # Ensure the component has the appropriate technology
            if pf.config.default_technology is not None:
                new_component_translated.technology = pf.config.default_technology

            # Get new bounds after translation
            new_bounds = new_component_translated.bounds()

            # Restore original warning behavior
            warnings.filters = original_warning_filter
            warnings.showwarning = original_showwarning

            # Now it's safe to process warnings without risking recursion
            # Just log the first few warnings to avoid overloading the message system
            if self.warning_handler.warnings:
                max_warnings_to_show = 5  # Limit number of warnings we display
                for i, warning in enumerate(self.warning_handler.warnings[:max_warnings_to_show]):
                    # Truncate warning messages that are too long
                    if len(warning) > 1000:
                        warning = warning[:1000] + "... (truncated)"
                    self.log_warning(warning)

                if len(self.warning_handler.warnings) > max_warnings_to_show:
                    self.log_warning(
                        f"... and {len(self.warning_handler.warnings) - max_warnings_to_show} more warnings (suppressed)"
                    )

                # Clear warnings after processing
                self.warning_handler.warnings = []

            # Add the new component to our components dictionary
            self.add_component(new_component_translated, component_name)

            # Return success with bounds information for debugging
            return {
                "message": f"Component '{component_name}' saved successfully",
                "original_bounds": [
                    [float(bounds[0][0]), float(bounds[0][1])],
                    [float(bounds[1][0]), float(bounds[1][1])],
                ],
                "new_bounds": [
                    [float(new_bounds[0][0]), float(new_bounds[0][1])],
                    [float(new_bounds[1][0]), float(new_bounds[1][1])],
                ],
            }

        except Exception as e:
            # Restore original warning behavior even if there's an error
            warnings.filters = original_warning_filter
            warnings.showwarning = original_showwarning

            error_msg = f"Error saving component '{data.get('name', 'unknown')}': {str(e)}"
            self.log_error(error_msg)
            traceback.print_exc()
            # Ensure we only return a string representation of the error
            return {"error": str(e)[:1000]}, 500

    async def _delete_component(self, data):
        """Delete a component"""
        try:
            component_name = data.get("name")

            if not component_name:
                error_msg = "Component name is required"
                self.log_error(error_msg)
                return {"error": error_msg}, 400

            # Check if the component exists
            if component_name not in self.components:
                error_msg = f"Component '{component_name}' not found"
                self.log_error(error_msg)
                return {"error": error_msg}, 404

            # Check if it's a built-in component
            builtin_components = [
                "chip_frame",
                "cpw_probe_pad_linear",
                "dir_coupl",
                "double_linear_inverse_taper",
                "eo_phase_shifter",
                "heated_straight_waveguide",
                "heater_pad",
                "heater_straight",
                "l_turn_bend",
                "mmi1x2",
                "mmi2x2",
                "mz_modulator_unbalanced",
                "s_bend_var_width",
                "s_bend_vert",
                "u_bend_racetrack",
                "u_turn_bend",
            ]

            if component_name in builtin_components:
                error_msg = "Cannot delete built-in components"
                self.log_error(error_msg)
                return {"error": error_msg}, 403

            # Delete the component
            self.remove_component(component_name)

            return {"message": f"Component '{component_name}' deleted successfully"}

        except Exception as e:
            error_msg = f"Error deleting component '{data.get('name', 'unknown')}': {str(e)}"
            self.log_error(error_msg)
            traceback.print_exc()
            return {"error": str(e)}, 500

    def _run_server(self):
        """Run the FastAPI server in a separate thread"""
        # Set log level to 'error' to suppress most logs
        uvicorn.run(self.app, host="0.0.0.0", port=self.port, log_level="error")

    def start(self):
        """Start the server in a separate thread"""
        if self.server_thread is None or not self.server_thread.is_alive():
            self.server_thread = threading.Thread(target=self._run_server)
            self.server_thread.daemon = True
            self.server_thread.start()

    def stop(self):
        """Stop the server (note: this is not fully implemented in this version)"""
        # In a production version, you would need a proper way to stop the uvicorn server
        pass

    def add_component(self, component, name=None):
        """Add a component to the editor"""
        if name is None:
            name = component.name
        self.components[name] = component
        self._notify_clients()
        return self

    def remove_component(self, name):
        """Remove a component from the editor"""
        if name in self.components:
            del self.components[name]
            self._notify_clients()
        return self

    def _notify_clients(self):
        """Notify all connected clients about component changes"""
        # Get the updated component information
        components_info = self._get_components_info()

        # Create a background task to send the update to all clients
        async def send_update():
            # Send to all connected clients
            for client_id, client_queue in list(self.clients.items()):
                try:
                    await client_queue.put(components_info)
                except Exception:
                    # Remove problematic clients
                    if client_id in self.clients:
                        del self.clients[client_id]

        # Create and run the task in the event loop
        try:
            # If we're already in an async context
            asyncio.create_task(send_update())
        except RuntimeError:
            # If we're not in an async context (e.g., called from Jupyter)
            try:
                loop = asyncio.get_event_loop()
            except RuntimeError:
                # If there's no event loop in this thread, create a new one
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)

            # Run the coroutine in the event loop
            _ = asyncio.run_coroutine_threadsafe(send_update(), loop)

    def start_frontend(self):
        """Start the frontend development server"""
        try:
            # Get the directory of the frontend app
            current_dir = os.path.dirname(os.path.abspath(__file__))
            frontend_dir = os.path.join(current_dir, "schematic_editor")

            if not os.path.exists(frontend_dir):
                self.log_warning(f"Frontend directory not found at {frontend_dir}")
                return False

            cmd = ["python", "-m", "http.server", str(self.frontend_port), "-d", frontend_dir]

            # Start the frontend process
            self.frontend_process = subprocess.Popen(
                cmd,
                cwd=frontend_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
            )

            # Start a thread to monitor the process output
            def monitor_output():
                for line in self.frontend_process.stdout:
                    pass
                for line in self.frontend_process.stderr:
                    error_msg = f"Frontend Error: {line.strip()}"
                    self.log_error(error_msg)

            threading.Thread(target=monitor_output, daemon=True).start()

            # Wait a moment to see if the process starts successfully
            time.sleep(2)
            if self.frontend_process.poll() is not None:
                error_msg = "Frontend process failed to start"
                self.log_error(error_msg)
                return False

            print(f"Schematic Editor is running at localhost:{self.frontend_port}")
            return True

        except Exception as e:
            error_msg = f"Error starting frontend: {str(e)}"
            self.log_error(error_msg)
            traceback.print_exc()
            return False

    def stop_frontend(self):
        """Stop the frontend server"""
        if self.frontend_process:
            try:
                # Try to terminate gracefully first
                if os.name == "nt":  # Windows
                    self.frontend_process.terminate()
                else:  # Unix/Linux/Mac
                    os.killpg(os.getpgid(self.frontend_process.pid), signal.SIGTERM)

                # Wait a bit for graceful shutdown
                time.sleep(1)

                # Force kill if still running
                if self.frontend_process.poll() is None:
                    if os.name == "nt":  # Windows
                        self.frontend_process.kill()
                    else:  # Unix/Linux/Mac
                        os.killpg(os.getpgid(self.frontend_process.pid), signal.SIGKILL)

            except Exception as e:
                error_msg = f"Error stopping frontend: {str(e)}"
                self.log_error(error_msg)
                traceback.print_exc()
            finally:
                self.frontend_process = None

    def cleanup(self):
        """Clean up resources when the program exits"""
        self.stop_frontend()
        self.stop()

    def __str__(self):
        frontend_url = f"http://localhost:{self.frontend_port}"
        return f"SchematicEditor - Frontend: {frontend_url}"

    def _repr_html_(self):
        """Returns clickable link for Jupyter"""
        frontend_url = f"http://localhost:{self.frontend_port}"
        return f"""
        <div>
            <p>PhotonForge Schematic Editor is running at:<br/>
            <a href="{frontend_url}" target="_blank">{frontend_url}</a></p>
        </div>
        """


# For backwards compatibility
def run_server(port=8000):
    """Run the schematic editor server (legacy function)"""
    editor = SchematicEditor(port=port)
    return editor
