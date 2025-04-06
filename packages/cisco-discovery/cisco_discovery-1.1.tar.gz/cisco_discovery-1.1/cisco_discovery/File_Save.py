import pandas as pd
import os
from datetime import datetime

from .Draw_io import draw_io_xml_generate

class SaveFile:
    def __init__(self, file_format, src_type, src_content: dict, directory: str="output", file_name: str=""):
        self.file_format = file_format
        self.src_type = src_type 
        self.src_content = src_content
        self.directory = directory
        self.file_name = file_name
        self.nodes_record_list = []
        self.edges_record_list = []
        
        
        # create directory if not present
        os.makedirs(self.directory, exist_ok=True)
        
        # check if / in directory end
        if self.directory.endswith('/'):
            self.directory = self.directory[:-1]
        
        # set default filename if none is provided
        if not self.file_name:
            self.file_name = datetime.now().strftime(r"%d_%m_%Y__%I-%M_%p")
        
        if not isinstance(self.src_content, dict) and not self.src_content:
            raise BaseException("invalid src_content")
    
    def generate(self):
        if self.src_type == "nodes":
            self.process_nodes(self.src_content)
            self.save_file("nodes")
        if self.src_type == "edges":
            self.process_edges(self.src_content)
            self.save_file("edges")
        
        if self.src_type == "nodes-edges":
            nodes_content = self.src_content.get('nodes', None)
            edges_content = self.src_content.get('edges', None)
            
            if not nodes_content or not edges_content:
                raise BaseException("nodes_content or edges_content is not dict")
            
            self.process_nodes(nodes_content)
            self.process_edges(edges_content)
            self.save_file("nodes")
            self.save_file("edges")
        
        if self.src_type == "draw_io":
            nodes_content = self.src_content.get('nodes', None)
            edges_content = self.src_content.get('edges', None)
            
            if not nodes_content or not edges_content:
                raise BaseException("nodes_content or edges_content is not dict")
            
            self.process_nodes(nodes_content)
            self.process_edges(edges_content)
            self.save_file("draw_io")
            
            
    def process_nodes(self, src_content):
        nodes = src_content
        # Clear data
        self.nodes_record_list = []
        for node in nodes:
            self.nodes_record_list.append({
                'node': node,
                'role': nodes[node].get('role', None),
                'mgmt': " ".join(nodes[node]['mgmt']) if nodes[node].get('mgmt', None) else None,
                'login': nodes[node].get('login', None),
                'discovered': nodes[node].get('discovered', None),
            })
        
    def process_edges(self, src_content):
        edges = src_content
        # Clear data
        self.edges_record_list = []
        for edge in edges:
            a_node = edge
            a_ports = edges[edge]
            
            for a_port in a_ports:
                b_nodes = a_ports[a_port]
                for b_node in b_nodes:
                    b_port = b_nodes[b_node]
                    self.edges_record_list.append({
                        'a_node': a_node,
                        'a_port': a_port,
                        'b_node': b_node,
                        'b_port': b_port
                    })
    
    def save_file(self, src_type):
        
        if self.file_format == 'csv':
            encoding = "utf-8"
            
            if src_type == "nodes":
                df = pd.DataFrame(self.nodes_record_list)
                col = ['node', 'role', 'mgmt', 'login', 'discovered']
                df = df[col]
                file_full_path = f"{self.directory}/nodes_{self.file_name}.csv"
                df.to_csv(file_full_path, encoding=encoding, index=False)
                return f"save to {file_full_path}"
            
            if src_type == "edges":
                df = pd.DataFrame(self.edges_record_list)
                col = ['a_node', 'a_port', 'b_node', 'b_port']
                df = df[col]
                file_full_path = f"{self.directory}/edges_{self.file_name}.csv"
                df.to_csv(file_full_path, encoding=encoding, index=False)
                return f"save to {file_full_path}"
        
        if self.file_format == 'excel':
            
            if src_type == "nodes":
                df = pd.DataFrame(self.nodes_record_list)
                col = ['node', 'role', 'mgmt', 'login', 'discovered']
                df = df[col]
                file_full_path = f"{self.directory}/nodes_{self.file_name}.xlsx"
                df.to_excel(file_full_path, index=False)
                return f"save to {file_full_path}"
            
            if src_type == "edges":
                df = pd.DataFrame(self.edges_record_list)
                col = ['a_node', 'a_port', 'b_node', 'b_port']
                df = df[col]
                file_full_path = f"{self.directory}/edges_{self.file_name}.xlsx"
                df.to_excel(file_full_path, index=False)
                return f"save to {file_full_path}"
        
        if self.file_format == 'draw_io':
            
            if src_type == "draw_io":
                file_full_path = f"{self.directory}/{self.file_name}.drawio"
                draw_io_save = draw_io_xml_generate(self.nodes_record_list, self.edges_record_list, file_full_path)
                if draw_io_save:
                    return (f"\nSuccessfully saved diagram to {file_full_path}")
            
class NODES_TO_CSV(SaveFile):
    def __init__(self, src_content, directory = "output", file_name = ""):
        super().__init__("csv", "nodes", src_content, directory, file_name)

class NODES_TO_EXCEL(SaveFile):
    def __init__(self, src_content, directory = "output", file_name = ""):
        super().__init__("excel", "nodes", src_content, directory, file_name)

class EDGES_TO_CSV(SaveFile):
    def __init__(self, src_content, directory = "output", file_name = ""):
        super().__init__("csv", "edges", src_content, directory, file_name)

class EDGES_TO_EXCEL(SaveFile):
    def __init__(self, src_content, directory = "output", file_name = ""):
        super().__init__("excel", "edges", src_content, directory, file_name)
        

class NODES_EDGES_TO_CSV(SaveFile):
    def __init__(self, src_content, directory = "output", file_name = ""):
        super().__init__("csv", "nodes-edges", src_content, directory, file_name)

class NODES_EDGES_TO_EXCEL(SaveFile):
    def __init__(self, src_content, directory = "output", file_name = ""):
        super().__init__("excel", "nodes-edges", src_content, directory, file_name)
        
class NODES_EDGES_TO_DRAW_IO(SaveFile):
    def __init__(self, src_content, directory = "output", file_name = ""):
        super().__init__("draw_io", "draw_io", src_content, directory, file_name)