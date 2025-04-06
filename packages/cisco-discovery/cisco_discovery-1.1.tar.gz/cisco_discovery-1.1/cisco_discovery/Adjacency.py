class Adjacency:
    def __init__(self, protocol, neighbor_table):
        self.protocol = protocol
        self.neighbor_table = neighbor_table
        self.neighbor_map = None
        self.neighbor = None
        
        self.to_dict()
        
        if not self.neighbor_table and not isinstance(self.neighbor_table, dict):
            raise Exception(f"Invalid neighbor table data is provided")
        
        if self.protocol not in ['cdp', 'lldp']:
            raise Exception(f"Protocol invalid, use cdp or lldp")
        
        self.process()
    
    def to_dict(self):
        try:
            self.neighbor_table = dict(self.neighbor_table)
        except TypeError:
            pass
        
    def process(self):
        if self.protocol in ['cdp']:
            if not self.neighbor_table.get('index', None):
                raise ValueError(f"cdp structured data is corrput")
            
            local_dict = {}
            local_dict_neighbor = {}
            neighbors = self.neighbor_table['index']
            
            # read all indexes
            for i in neighbors:
                if "AP" in neighbors[i].get('software_version', None):
                    device_id = neighbors[i].get('device_id', '').upper()
                    if len(device_id) != 16 and not device_id.startswith("AP"):
                        device_id = neighbors[i].get('device_id', '').split('.')[0].split('(')[0].split(')')[0].upper()
                
                if "AP" not in neighbors[i].get('software_version', None):
                    device_id = neighbors[i].get('device_id', '').split('.')[0].split('(')[0].split(')')[0].upper()
                
                # insert device_id in local_dict
                local_interface = neighbors[i].get('local_interface', None)
                remote_port = neighbors[i].get('port_id', None)
                platform = neighbors[i].get('platform', '').split(' ')[-1]
                capabilities = neighbors[i].get('capabilities', None)
                
                local_dict[local_interface] = {'remote_port': remote_port,
                                               'platform': platform,
                                               'device_id': device_id,
                                               'capabilities': capabilities,
                                               'device_role': self.device_role(capabilities)}
                
                # Neighbor record
                if not local_dict_neighbor.get(device_id, None):
                    local_dict_neighbor[device_id] = {}
                
                if not local_dict_neighbor.get(device_id, {}).get('capabilities', None):
                    local_dict_neighbor[device_id]['capabilities'] = capabilities
                    local_dict_neighbor[device_id]['device_role'] = self.device_role(capabilities)
                
                # Management IP
                mgmt_ip = neighbors[i].get('management_addresses', None)
                if mgmt_ip:
                    my_ip = []
                    for ip in mgmt_ip:
                        my_ip.append(ip)
                    
                    if my_ip:
                        local_dict_neighbor[device_id]['mgmt'] = my_ip
            
            if local_dict:
                self.neighbor_map = local_dict
            
            if local_dict_neighbor:
                self.neighbor = local_dict_neighbor
    
    def device_role(self, capabilities="", platform=""):
        capabilities = capabilities.lower()
        platform = platform.lower()
        if "phone" in capabilities:
            return "phone"
        if "router switch igmp" in capabilities:
            return "switch"
        if "router trans-bridge" in capabilities:
            return "access-point"
        if "router" in capabilities:
            return "router"
        if "switch" in capabilities:
            return "switch"
        
        return "unknown"
        
class CDP_Adjacency(Adjacency):
    def __init__(self, neighbor_table):
        super().__init__("cdp", neighbor_table)
                    
class LLDP_Adjacency(Adjacency):
    def __init__(self, neighbor_table):
        super().__init__("lldp", neighbor_table)        
            
    