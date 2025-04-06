class Device_Role:
    def __init__(self, version) -> None:
        self.version = None
        self.role = None
        self.os = None
        
        self.to_dict(version)
        
        if not isinstance(self.version, dict):
            raise Exception("version is not of type dict")
        
        self.detect()
        
    def to_dict(self, version):
        try:
            self.version = dict(version)
        except TypeError:
            pass
        
    def detect(self):
        # Cisco IOS and IOS-XE
        if self.version.get('version', None):
            # router
            if not self.version['version'].get('switch_num', None):
                self.role = "router"
                self.os = self.version['version'].get('os', None)
            
            # Switch 
            if self.version['version'].get('switch_num', None):
                switches = self.version['version']['switch_num']
                # Single
                if len(switches) == 1:
                    self.role = "switch"
                    self.os = self.version['version'].get('os', None)
                # Stacked Switch
                if len(switches) >= 2:
                    self.role = "multi-switch"
                    self.os = self.version['version'].get('os', None)
        
        # Cisco Nexus
        if self.version.get('platform', None):
            pass