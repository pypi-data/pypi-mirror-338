import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import datetime

# --- Configuration ---
DEFAULT_NODE_WIDTH = 70 
DEFAULT_NODE_HEIGHT = 50 
# --- MODIFIED: Default edge style with no arrows ---
DEFAULT_EDGE_STYLE_NO_ARROWS = "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;strokeWidth=1;endArrow=none;startArrow=none;"
# --- Style for curved multi-edges (also no arrows) ---
CURVED_MULTI_EDGE_STYLE_BASE = "edgeStyle=entityRelationEdgeStyle;curved=1;rounded=0;html=1;strokeWidth=1;endArrow=none;startArrow=none;"

DEFAULT_FALLBACK_NODE_STYLE = "rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=#666666;"

# --- Auto-Layout "Vertical Flow" Approximation Configuration ---
# (Used if x, y are not provided in node data)
AUTO_LAYOUT_ITEMS_PER_LEVEL = 3    # Fewer items per row for vertical feel
AUTO_LAYOUT_HORIZONTAL_SPACING = 180 # Moderate horizontal spacing
AUTO_LAYOUT_VERTICAL_SPACING = 150   # Vertical spacing between levels
AUTO_LAYOUT_MARGIN_X = 50            
AUTO_LAYOUT_MARGIN_Y = 50            

# --- Device Type to Draw.io Style Mapping ---
# (Keep the DEVICE_STYLES dictionary from the previous version)
DEVICE_STYLES = {
    "router": "shape=mxgraph.cisco.routers.router;html=1;pointerEvents=1;dashed=0;fillColor=#036897;strokeColor=#ffffff;strokeWidth=2;verticalLabelPosition=bottom;verticalAlign=top;align=center;outlineConnect=0;fontStyle=1;labelBackgroundColor=default;labelBorderColor=none;",
    "switch": "shape=mxgraph.cisco19.rect;prIcon=l2_switch;html=1;pointerEvents=1;dashed=0;fillColor=#036897;strokeColor=#ffffff;strokeWidth=2;verticalLabelPosition=bottom;verticalAlign=top;align=center;outlineConnect=0;fontStyle=1;labelBackgroundColor=default;labelBorderColor=none;",
    "multi-switch": "shape=mxgraph.cisco19.rect;prIcon=l2_switch;html=1;pointerEvents=1;dashed=0;fillColor=#6a00ff;strokeColor=#ffffff;strokeWidth=2;verticalLabelPosition=bottom;verticalAlign=top;align=center;outlineConnect=0;fontStyle=1;labelBackgroundColor=default;labelBorderColor=none;",
    "core-switch": "shape=mxgraph.cisco19.rect;prIcon=l3_switch;html=1;pointerEvents=1;dashed=0;fillColor=#AA272F;strokeColor=#ffffff;strokeWidth=2;verticalLabelPosition=bottom;verticalAlign=top;align=center;outlineConnect=0;fontStyle=1;labelBackgroundColor=default;labelBorderColor=none;",
    "phone": "shape=mxgraph.cisco19.ip_phone;html=1;pointerEvents=1;dashed=0;fillColor=#005073;strokeColor=#ffffff;strokeWidth=2;verticalLabelPosition=bottom;verticalAlign=top;align=center;outlineConnect=0;fontStyle=1;labelBackgroundColor=default;labelBorderColor=none;",
    "access-point": "shape=mxgraph.cisco19.wireless_access_point;html=1;pointerEvents=1;dashed=0;fillColor=#036897;strokeColor=#ffffff;strokeWidth=2;verticalLabelPosition=bottom;verticalAlign=top;align=center;outlineConnect=0;fontStyle=1;labelBackgroundColor=default;labelBorderColor=none;",
    "voice_router": "shape=mxgraph.cisco19.rect;prIcon=router_with_voice;html=1;pointerEvents=1;dashed=0;fillColor=#036897;strokeColor=#ffffff;strokeWidth=2;verticalLabelPosition=bottom;verticalAlign=top;align=center;outlineConnect=0;fontStyle=1;labelBackgroundColor=default;labelBorderColor=none;",
    "firewall": "shape=mxgraph.networks.firewall;html=1;pointerEvents=1;dashed=0;fillColor=#E01B10;strokeColor=#ffffff;strokeWidth=2;verticalLabelPosition=bottom;verticalAlign=top;align=center;outlineConnect=0;fontStyle=1;labelBackgroundColor=default;labelBorderColor=none;",
    "server": "shape=mxgraph.networks.server;html=1;pointerEvents=1;dashed=0;fillColor=#434547;strokeColor=#ffffff;strokeWidth=2;verticalLabelPosition=bottom;verticalAlign=top;align=center;outlineConnect=0;fontStyle=1;labelBackgroundColor=default;labelBorderColor=none;",
    "laptop": "shape=mxgraph.cisco.computers_and_peripherals.laptop;html=1;pointerEvents=1;dashed=0;fillColor=#739D0A;strokeColor=#ffffff;strokeWidth=2;verticalLabelPosition=bottom;verticalAlign=top;align=center;outlineConnect=0;fontStyle=1;labelBackgroundColor=default;labelBorderColor=none;",
    "pc": "shape=mxgraph.cisco.computers_and_peripherals.pc;html=1;pointerEvents=1;dashed=0;fillColor=#739D0A;strokeColor=#ffffff;strokeWidth=2;verticalLabelPosition=bottom;verticalAlign=top;align=center;outlineConnect=0;fontStyle=1;labelBackgroundColor=default;labelBorderColor=none;",
    "cloud": "shape=cloud;html=1;pointerEvents=1;dashed=0;fillColor=#B3B3B3;strokeColor=#ffffff;strokeWidth=2;verticalLabelPosition=bottom;verticalAlign=top;align=center;outlineConnect=0;fontStyle=1;labelBackgroundColor=default;labelBorderColor=none;",
}

# --- Helper Functions ---
def create_base_drawio_tree():
    """Creates the basic Draw.io XML structure."""
    # Using current timestamp
    now = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')[:-3] + 'Z' # Format Z precision
    
    mxfile = ET.Element('mxfile', host="app.diagrams.net", modified=now, agent="PythonDrawioGen/1.0", etag="auto", version="1.0", type="device")
    diagram = ET.SubElement(mxfile, 'diagram', id="diagram-1", name="Page-1")
    mxGraphModel = ET.SubElement(diagram, 'mxGraphModel', dx="1400", dy="800", grid="1", gridSize="10", guides="1", tooltips="1", connect="1", arrows="1", fold="1", page="1", pageScale="1", pageWidth="850", pageHeight="1100", math="0", shadow="0") # Portrait page for vertical flow
    root = ET.SubElement(mxGraphModel, 'root')
    ET.SubElement(root, 'mxCell', id="0")
    ET.SubElement(root, 'mxCell', id="1", parent="0")
    return mxfile, root

def add_node(root, node_id, label, x, y, style, width=DEFAULT_NODE_WIDTH, height=DEFAULT_NODE_HEIGHT):
    """Adds a node (mxCell vertex) to the XML root."""
    node_cell = ET.SubElement(root, 'mxCell', id=str(node_id), value=str(label), style=style, parent="1", vertex="1")
    ET.SubElement(node_cell, 'mxGeometry', x=str(x), y=str(y), width=str(width), height=str(height), **{'as': 'geometry'}) 
    return node_cell

def add_edge(root, edge_id, source_id, target_id, label="", style=DEFAULT_EDGE_STYLE_NO_ARROWS):
    """Adds an edge (mxCell edge) to the XML root using the default no-arrow style."""
    edge_cell = ET.SubElement(root, 'mxCell', id=str(edge_id), value=str(label), style=style, parent="1", source=str(source_id), target=str(target_id), edge="1")
    ET.SubElement(edge_cell, 'mxGeometry', relative="1", **{'as': 'geometry'})
    return edge_cell

def prettify_xml(elem):
    """Return a pretty-printed XML string for the Element."""
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    # Add encoding line? minidom might add it automatically. Check output.
    return reparsed.toprettyxml(indent="  ")


# --- Main Generation Logic ---

def generate_diagram(nodes_data, edges_data):
    """
    Generates Draw.io XML. Auto-assigns node positions approximating a vertical flow
    if x, y are not provided. Styles multiple edges between the same nodes with curves.
    Removes arrows from all edges.

    Args:
        nodes_data (list): Dictionaries for nodes ('node', 'node', 'role', optional 'x', 'y', etc.).
        edges_data (list): Dictionaries for edges ('a_node', 'b_node', optional 'label', 'style').
    Returns:
        str: A pretty-printed Draw.io XML string.
    """
    mxfile, root = create_base_drawio_tree()

    current_id = 2
    node_id_map = {}

    # --- Auto Layout Initialization ---
    current_level = 0 # Row in vertical flow
    current_item_in_level = 0 # Column in vertical flow
    layout_needed = not all('x' in node and 'y' in node for node in nodes_data)
    if layout_needed:
        print("Info: Node coordinates (x, y) not provided. Applying basic 'vertical flow' layout approximation.")

    # Add Nodes
    for i, node_info in enumerate(nodes_data):
        xml_id = str(current_id)
        node_id_map[node_info['node']] = xml_id
        node_label = node_info['node']
        device_type = node_info.get('role')

        # --- Determine Position ---
        if 'x' in node_info and 'y' in node_info:
            node_x = node_info['x']
            node_y = node_info['y']
        elif layout_needed:
            node_x = AUTO_LAYOUT_MARGIN_X + current_item_in_level * AUTO_LAYOUT_HORIZONTAL_SPACING
            node_y = AUTO_LAYOUT_MARGIN_Y + current_level * AUTO_LAYOUT_VERTICAL_SPACING
            current_item_in_level += 1
            if current_item_in_level >= AUTO_LAYOUT_ITEMS_PER_LEVEL:
                current_item_in_level = 0
                current_level += 1
        else:
            print(f"Warning: Could not determine position for node {node_info['node']}. Placing at default.")
            node_x = AUTO_LAYOUT_MARGIN_X
            node_y = AUTO_LAYOUT_MARGIN_Y

        # --- Determine Style ---
        node_style = node_info.get('style') or DEVICE_STYLES.get(device_type, DEFAULT_FALLBACK_NODE_STYLE)
        node_width = node_info.get('width', DEFAULT_NODE_WIDTH)
        node_height = node_info.get('height', DEFAULT_NODE_HEIGHT)

        add_node(root, xml_id, node_label, node_x, node_y, node_style, node_width, node_height)
        current_id += 1

    # --- Edge Processing ---
    edge_pair_counts = {} 
    edge_instance_index = {}
    for edge_info in edges_data:
        source_id = node_id_map.get(edge_info['a_node'])
        target_id = node_id_map.get(edge_info['b_node'])
        if source_id and target_id:
            pair = tuple(sorted((source_id, target_id)))
            edge_pair_counts[pair] = edge_pair_counts.get(pair, 0) + 1
            edge_instance_index[pair] = 0 

    # Add Edges
    for edge_info in edges_data:
        xml_id = str(current_id)
        source_xml_id = node_id_map.get(edge_info['a_node'])
        target_xml_id = node_id_map.get(edge_info['b_node'])

        if not source_xml_id or not target_xml_id:
            print(f"Warning: Skipping edge due to missing node ID mapping for source '{edge_info['a_node']}' or target '{edge_info['b_node']}'.")
            continue # Skip this edge if nodes don't exist

        edge_label = edge_info.get('label', "")
        # Start with the default NO ARROW style
        edge_style = edge_info.get('style', DEFAULT_EDGE_STYLE_NO_ARROWS) 

        # --- Apply curve for multiple edges ---
        pair = tuple(sorted((source_xml_id, target_xml_id)))
        if edge_pair_counts.get(pair, 0) > 1:
            instance_idx = edge_instance_index[pair]
            if instance_idx > 0: 
                # Use the dedicated curved style base, potentially adding other custom parts later if needed
                edge_style = CURVED_MULTI_EDGE_STYLE_BASE 
                # Future enhancement: could add slight geometric offsets here too if needed
                # e.g. entryDx/Dy based on instance_idx, but requires more complex style parsing/merging.
                # For now, just relying on curved=1 and entityRelationEdgeStyle difference.
            edge_instance_index[pair] += 1 

        # Ensure final style definitely has no arrows (in case custom style was provided)
        style_parts = [part for part in edge_style.split(';') if part]
        # Remove any existing arrow settings
        style_parts = [part for part in style_parts if not part.startswith('endArrow=') and not part.startswith('startArrow=')]
        # Add explicit no arrows
        style_parts.append("endArrow=none")
        style_parts.append("startArrow=none")
        # Remove duplicates just in case
        final_style = ";".join(sorted(list(set(style_parts)))) + ";" 
        # Ensure trailing semicolon for Draw.io compatibility
        if not final_style.endswith(';'):
             final_style += ';'


        add_edge(
            root,
            xml_id,
            source_xml_id,
            target_xml_id,
            edge_label,
            final_style # Use the processed style
        )
        current_id += 1

    # Add modification timestamp (already done in create_base_drawio_tree)
    # mxfile.set('modified', datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')) 

    return prettify_xml(mxfile)


def draw_io_xml_generate(nodes, edges, file_full_path):
    # 3. Generate the XML
    drawio_xml_output = generate_diagram(nodes, edges)

    # 4. Print or Save the XML
    try:
        with open(file_full_path, "w", encoding="utf-8") as f:
            f.write(drawio_xml_output)
        return (f"\nSuccessfully saved diagram to {file_full_path}")
    except IOError as e:
        print(f"\nError saving file: {e}")