import os
from multiprocessing.dummy import Pool as ThreadPool
from netmiko import ConnectHandler
from .Adjacency import CDP_Adjacency
from .Device_Role import Device_Role
from .Discovery import Discovery
from dotenv import load_dotenv

def connect(argument):
    obj_discovery = argument[0]
    host = argument[1]
    # Verify if host has previously scanned
    if obj_discovery.nodes and obj_discovery.nodes.get(host, {}).get('login', None) :
        # Host already login
        return
    
    remote_host = {
        "host": host,
        "device_type": "cisco_xe",
        "username": os.getenv("NETMIKO_USERNAME"),
        "password": os.getenv("NETMIKO_PASSWORD"),
        "fast_cli": False
    }
    try:
        net_connect  = ConnectHandler(**remote_host)
        hostname = net_connect.find_prompt().replace('>', '').replace('#', '').split('(')[0].upper()
        
        # add node in obj_discover
        obj_discovery.add_node(hostname)
        obj_discovery.nodes[hostname]['login'] = True
        
        # Version for device type as router or switch
        show_version = net_connect.send_command("show version", use_genie=True, read_timeout=300)
        obj_device_role = Device_Role(show_version)
        
        # Update device_role
        if not obj_discovery.nodes[hostname].get('role', None):
            obj_discovery.nodes[hostname]['role'] = obj_device_role.role
        
        print(f"Current device: {hostname}, role: {obj_device_role.role}")
        
        # CDP neighbors
        show_cdp_neighbor = net_connect.send_command("show cdp neighbors detail", use_genie=True, read_timeout=300)
        
        obj_cdp = CDP_Adjacency(show_cdp_neighbor)
        
        # adding nodes in discovery object
        if obj_cdp.neighbor:
            for node in obj_cdp.neighbor:
                obj_discovery.add_node(node)
                role = obj_cdp.neighbor[node].get('device_role', None)
                mgmt = obj_cdp.neighbor[node].get('mgmt', None)
                if role and not obj_discovery.nodes[node].get('role', None):
                    obj_discovery.nodes[node]['role'] = role
                    obj_discovery.nodes[node]['mgmt'] = mgmt
        
        # adding edges in discovery object
        if obj_cdp.neighbor_map:
            for edge in obj_cdp.neighbor_map:
                node_a = hostname
                port_a = edge
                node_b = obj_cdp.neighbor_map[edge].get('device_id', None)
                port_b = obj_cdp.neighbor_map[edge].get('remote_port', None)
                
                if node_a and port_a and node_b and port_b:
                    obj_discovery.add_edge(node_a, port_a, node_b, port_b)
                    
        obj_discovery.nodes[hostname]['discovered'] = True
        net_connect.disconnect()
    except Exception as e:
        if not obj_discovery.nodes:
            print(f"Failed to connect to provided host: {host}")
            return
        obj_discovery.failed_update(host)
        

def run_commands_threaded(obj_discovery, devices, max_threads=5):
    """Runs commands on multiple devices using threads, controlling the number of threads."""
    
    argument_map = [(obj_discovery, device) for device in devices]
    
    threads = ThreadPool(max_threads)
    results = threads.map(connect, argument_map)
    threads.close()
    threads.join()
    
def runner(host: str, threads: int=5 , username:str="", password: str="" , env: str=""):
    
    if not host:
        raise ValueError("host missing")
    obj_discovery = Discovery()
    
    # Activate env variables
    if env:
        load_dotenv(dotenv_path = env)
    
    # Check credentials
    if username and password:
        os.environ["NETMIKO_USERNAME"] = username
        os.environ["NETMIKO_PASSWORD"] = password
        
    if not os.getenv("NETMIKO_USERNAME") or not os.getenv("NETMIKO_PASSWORD"):
        raise ValueError("credentials missing")
    
    flag = False
    while(not flag):
        if not obj_discovery.nodes:
            run_commands_threaded(obj_discovery, [host], max_threads=threads)
            if not obj_discovery.nodes:
                return
        if obj_discovery.nodes:
            # generate target device list
            obj_discovery.next_target()
            if obj_discovery.next_target_devices:
                run_commands_threaded(obj_discovery, obj_discovery.next_target_devices, max_threads=threads)
            if not obj_discovery.next_target_devices:
                # Break loop
                obj_discovery.full_nodes_edges()
                flag = True
                
    return obj_discovery