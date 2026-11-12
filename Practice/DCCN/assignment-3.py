class RouterInterface:
    pass
class Host:
    pass
class LAN:
    def __init__(self,name):
        self.name = name
        self.devices = []
        
    def add_device(self,device):
        self.devices.append(device)
        
    def broadcast(self,sender,message):
        print(f"BROADCASTING ON {self.name}")
        print(f"{sender.name} -> FF:FF:FF:FF:FF:FF")
        print(f"MESSAGE : {message}")
        
        
        for device in self.devices:
            if hasattr(device,"recieve_broadcast"):
                device.recieve_broadcast(message)
                
    def get_router_by_mac(self,mac):
        for device in self.devices:
            if isinstance(device,RouterInterface):
                if device.mac == mac:
                    return device.router
                
        return None
    
    def deliver_packet(self,sender,destination_mac,destination_ip,data):
        print(f"LAN DELIVERY ON {self.name}")
        
        for device in self.devices:
            if device.mac == destination_mac:
                print(f"PACKET RECIEVED BY : {device.name}")
                
                if isinstance(device,Host):
                    device.recieve_packet(sender,destination_ip,data)
                
                return
        return "destination mac not found"
                    
    def handle_arp_request(self,sender,target_ip):
        pass