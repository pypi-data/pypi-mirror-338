
from .File_Save import EDGES_TO_CSV, EDGES_TO_EXCEL, NODES_EDGES_TO_CSV, NODES_EDGES_TO_DRAW_IO, NODES_EDGES_TO_EXCEL, NODES_TO_CSV, NODES_TO_EXCEL


class Discovery:
    def __init__(self):
        self.nodes = None
        self.edges = None
        self.node_edges = None
        self.next_target_devices = None
    
    def add_node(self, node):
        # for first node
        if not self.nodes:
            self.nodes = {node: {}}
        
        if self.nodes:
            # check exisiting entry
            if not self.nodes.get(node, None):
                self.nodes[node] = {}
    
    def add_edge(self, node_a, port_a, node_b, port_b):
        # for first edge
        if not self.edges:
            self.edges = {}
            self.edges[node_a] = {port_a: {node_b: port_b}}
        
        if self.edges:
            # check existing entry
            if not self.edges.get(node_a, None) and not self.edges.get(node_b, None):
                self.edges[node_a] = {}
                
            if not self.edges.get(node_a, {}).get(port_a, None):
                if not self.edges.get(node_b, {}).get(port_b, None):
                    self.edges[node_a][port_a] = {node_b: port_b}
    
    def insert_bulk_adjacency(self, node_a:str, adjacency: dict):
        
        if adjacency and isinstance(adjacency, dict):
            for edge in adjacency:
                node_a = node_a
                port_a = edge
                node_b = adjacency[edge].get('device_id', None)
                port_b = adjacency[edge].get('remote_port', None)
                
                if node_a and port_a and node_b and port_b:
                    self.add_edge(node_a, port_a, node_b, port_b)
    
    def next_target(self):
        if self.nodes:
            device_list = []
            for i in self.nodes:
                # remove based on roles
                if self.nodes[i].get('role', None) in ['switch', 'router', 'multi-switch'] and not self.nodes[i].get('login', None):
                    # has valid mgmt
                    if isinstance(self.nodes[i].get('mgmt', None), list) and self.nodes[i].get('mgmt', None):
                        mgmt = self.nodes[i]['mgmt']
                        for ip in mgmt:
                            device_list.append(ip)
                        
            self.next_target_devices = device_list
    
    def failed_update(self, mgmt_ip):
        if self.nodes:
            for i in self.nodes:
                # has valid mgmt
                if isinstance(self.nodes[i].get('mgmt', None), list) and self.nodes[i].get('mgmt', None):
                    mgmt = self.nodes[i]['mgmt']
                    for ip in mgmt:
                        if ip == mgmt_ip:
                            self.nodes[i]['login'] = "Error"
    
    def full_nodes_edges(self):
        self.node_edges = {"nodes": self.nodes,
                           "edges": self.edges}
    
    def to_csv_nodes(self, directory = "output", file_name = ""):
        if self.nodes:
            obj_nodes = NODES_TO_CSV(src_content=self.nodes, directory=directory, file_name=file_name)
            return obj_nodes.generate()
            
    def to_excel_nodes(self, directory = "output", file_name = ""):
        if self.nodes:
            obj_nodes = NODES_TO_EXCEL(src_content=self.nodes, directory=directory, file_name=file_name)
            return obj_nodes.generate()
    
    def to_csv_edges(self, directory = "output", file_name = ""):
        if self.edges:
            obj_edges = EDGES_TO_CSV(src_content=self.edges, directory=directory, file_name=file_name)
            return obj_edges.generate()
        
    def to_excel_edges(self, directory = "output", file_name = ""):
        if self.edges:
            obj_edges = EDGES_TO_EXCEL(src_content=self.edges, directory=directory, file_name=file_name)
            return obj_edges.generate()
    
    def to_csv(self, directory = "output", file_name = ""):
        if self.node_edges:
            obj_node_edges = NODES_EDGES_TO_CSV(src_content=self.node_edges, directory=directory, file_name=file_name)
            return obj_node_edges.generate()
        
    def to_excel(self, directory = "output", file_name = ""):
        if self.node_edges:
            obj_node_edges = NODES_EDGES_TO_EXCEL(src_content=self.node_edges, directory=directory, file_name=file_name)
            return obj_node_edges.generate()
    
    def to_draw_io(self, directory = "output", file_name = ""):
        if self.node_edges:
            obj_node_edges = NODES_EDGES_TO_DRAW_IO(src_content=self.node_edges, directory=directory, file_name=file_name)
            return obj_node_edges.generate()
    
    def __str__(self):
        return "Class for building nodes and edges"
