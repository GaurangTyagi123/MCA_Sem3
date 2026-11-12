import time
import ipaddress


# ============================================================
# IP PACKET
# ============================================================

class IPPacket:
    def __init__(self, source_ip, destination_ip, data, ttl=5):
        self.source_ip = source_ip
        self.destination_ip = destination_ip
        self.data = data
        self.ttl = ttl

    def __str__(self):
        return (
            f"IP Packet: "
            f"{self.source_ip} -> {self.destination_ip}, "
            f"TTL={self.ttl}"
        )


# ============================================================
# HOST
# ============================================================

class Host:

    def __init__(
        self,
        name,
        mac,
        ip=None,
        gateway=None,
        subnet_mask="255.255.255.0"
    ):
        self.name = name
        self.mac = mac
        self.ip = ip
        self.gateway = gateway
        self.subnet_mask = subnet_mask

        # ARP cache:
        # IP -> (MAC, expiry_time)
        self.arp_cache = {}

    # --------------------------------------------------------
    # NETWORK
    # --------------------------------------------------------

    def get_network(self):
        network = ipaddress.ip_network(
            f"{self.ip}/{self.subnet_mask}",
            strict=False
        )

        return network

    # --------------------------------------------------------
    # BROADCAST
    # --------------------------------------------------------

    def receive_broadcast(self, message):
        print(f"{self.name} received broadcast: {message}")

    # --------------------------------------------------------
    # RARP
    # --------------------------------------------------------

    def rarp_request(self, rarp_server):

        print(f"\n[RARP REQUEST] {self.name}")
        print(f"    Source MAC: {self.mac}")
        print(f"    Destination: FF:FF:FF:FF:FF:FF")
        print(f"    Question: What is the IP address for {self.mac}?")

        rarp_server.receive_rarp_request(
            self,
            self.mac
        )

    # --------------------------------------------------------
    # ARP
    # --------------------------------------------------------

    def arp_request(self, target_ip, lan, ttl=5):

        print(f"\n[ARP] {self.name} wants MAC for {target_ip}")

        # ----------------------------------------------------
        # Check ARP cache
        # ----------------------------------------------------

        if target_ip in self.arp_cache:

            mac, expiry = self.arp_cache[target_ip]

            if time.time() < expiry:

                print("[ARP CACHE HIT]")
                print(f"    {target_ip} -> {mac}")

                return mac

            else:

                print("[ARP CACHE EXPIRED]")

                # Remove expired entry
                del self.arp_cache[target_ip]

        # ----------------------------------------------------
        # ARP cache miss
        # ----------------------------------------------------

        print("[ARP CACHE MISS]")
        print(f"[ARP REQUEST] Who has {target_ip}?")

        mac = lan.handle_arp_request(
            self,
            target_ip
        )

        # ----------------------------------------------------
        # Update ARP cache
        # ----------------------------------------------------

        if mac is not None:

            self.arp_cache[target_ip] = (
                mac,
                time.time() + ttl
            )

            print("[ARP CACHE UPDATE]")
            print(f"    {target_ip} -> {mac}")
            print(f"    TTL = {ttl} seconds")

            return mac

        print("[ARP FAILURE]")
        print(f"    No host owns IP {target_ip}")

        return None

    # --------------------------------------------------------
    # SEND PACKET
    # --------------------------------------------------------

    def send_packet(self, destination_ip, data, lan):

        print("\n" + "=" * 60)
        print(f"[SEND PACKET] {self.name}")

        print(f"    Source IP      : {self.ip}")
        print(f"    Destination IP : {destination_ip}")

        destination = ipaddress.ip_address(destination_ip)

        # ====================================================
        # CASE 1: DESTINATION IS ON LOCAL SUBNET
        # ====================================================

        if destination in self.get_network():

            print("[ROUTING] Destination is on local subnet.")

            target_ip = destination_ip

            # ARP for destination host
            target_mac = self.arp_request(
                target_ip,
                lan
            )

            if target_mac is None:

                print("[PACKET] Delivery failed.")

                return

            # Create IP packet
            packet = IPPacket(
                self.ip,
                destination_ip,
                data
            )

            print("\n[ETHERNET FRAME]")
            print(f"    Source MAC      : {self.mac}")
            print(f"    Destination MAC : {target_mac}")

            # Deliver frame directly
            lan.deliver_packet(
                self,
                target_mac,
                destination_ip,
                data
            )

        # ====================================================
        # CASE 2: DESTINATION IS ON REMOTE SUBNET
        # ====================================================

        else:

            print("[ROUTING] Destination is on remote subnet.")

            if self.gateway is None:

                print("[ROUTING FAILURE]")
                print("    No default gateway configured.")

                return

            print(f"[ROUTING] Using gateway {self.gateway}")

            # ------------------------------------------------
            # ARP for gateway
            # ------------------------------------------------

            gateway_mac = self.arp_request(
                self.gateway,
                lan
            )

            if gateway_mac is None:

                print("[PACKET] Gateway MAC resolution failed.")

                return

            # ------------------------------------------------
            # Create IP packet
            # ------------------------------------------------

            packet = IPPacket(
                self.ip,
                destination_ip,
                data
            )

            print("\n[ETHERNET FRAME]")
            print(f"    Source MAC      : {self.mac}")
            print(f"    Destination MAC : {gateway_mac}")

            # ------------------------------------------------
            # Find the router connected to this LAN
            # ------------------------------------------------

            router = lan.get_router_by_mac(gateway_mac)

            if router is None:

                print("[PACKET] Router not found on LAN.")

                return

            # ------------------------------------------------
            # Give packet to router
            # ------------------------------------------------

            router.receive_packet(
                packet,
                self.mac,
                gateway_mac,
                lan
            )

    # --------------------------------------------------------
    # RECEIVE PACKET
    # --------------------------------------------------------

    def receive_packet(self, sender, destination_ip, data):

        print("\n[PACKET RECEIVED]")

        print(f"    Receiver        : {self.name}")
        print(f"    Source          : {sender.ip}")
        print(f"    Destination     : {destination_ip}")
        print(f"    Data            : {data}")

    # --------------------------------------------------------
    # STRING
    # --------------------------------------------------------

    def __str__(self):

        return (
            f"{self.name} | "
            f"IP: {self.ip} | "
            f"MAC: {self.mac}"
        )


# ============================================================
# LAN
# ============================================================

class LAN:

    def __init__(self, name):

        self.name = name
        self.devices = []

    # --------------------------------------------------------
    # ADD DEVICE
    # --------------------------------------------------------

    def add_device(self, device):

        self.devices.append(device)

    # --------------------------------------------------------
    # BROADCAST
    # --------------------------------------------------------

    def broadcast(self, sender, message):

        print(f"\n[BROADCAST on {self.name}]")
        print(f"{sender.name} -> FF:FF:FF:FF:FF:FF")
        print(f"Message: {message}")

        for device in self.devices:

            if device != sender:

                # Only devices that implement
                # receive_broadcast can receive it
                if hasattr(device, "receive_broadcast"):

                    device.receive_broadcast(message)

    # --------------------------------------------------------
    # FIND ROUTER
    # --------------------------------------------------------

    def get_router_by_mac(self, mac):

        for device in self.devices:

            if isinstance(device, RouterInterface):

                if device.mac == mac:

                    return device.router

        return None

    # --------------------------------------------------------
    # DELIVER ETHERNET FRAME
    # --------------------------------------------------------

    def deliver_packet(
        self,
        sender,
        destination_mac,
        destination_ip,
        data
    ):

        print(f"\n[LAN DELIVERY on {self.name}]")

        for device in self.devices:

            if device.mac == destination_mac:

                print(
                    f"    Frame delivered to: "
                    f"{device.name}"
                )

                # Normal Host
                if isinstance(device, Host):

                    device.receive_packet(
                        sender,
                        destination_ip,
                        data
                    )

                return

        print("    Destination MAC not found.")

    # --------------------------------------------------------
    # ARP REQUEST
    # --------------------------------------------------------

    def handle_arp_request(self, sender, target_ip):

        print(f"\n[BROADCAST on {self.name}]")

        print(f"    Sender        : {sender.name}")
        print(f"    Sender IP     : {sender.ip}")
        print(f"    Sender MAC    : {sender.mac}")
        print(f"    Destination   : FF:FF:FF:FF:FF:FF")
        print(f"    Question      : Who has {target_ip}?")

        for device in self.devices:

            if device == sender:

                continue

            # ------------------------------------------------
            # Normal host
            # ------------------------------------------------

            if isinstance(device, Host):

                if device.ip == target_ip:

                    print(
                        f"\n[ARP REPLY from {device.name}]"
                    )

                    print(f"    IP  : {target_ip}")
                    print(f"    MAC : {device.mac}")
                    print("    Delivery: UNICAST")

                    return device.mac

            # ------------------------------------------------
            # Router interface
            # ------------------------------------------------

            if isinstance(device, RouterInterface):

                if device.ip == target_ip:

                    print(
                        f"\n[ARP REPLY from ROUTER]"
                    )

                    print(f"    Interface : {device.name}")
                    print(f"    IP        : {device.ip}")
                    print(f"    MAC       : {device.mac}")
                    print("    Delivery  : UNICAST")

                    return device.mac

        return None


# ============================================================
# ROUTER INTERFACE
# ============================================================

class RouterInterface:

    def __init__(
        self,
        name,
        ip,
        mac,
        network,
        lan=None
    ):

        self.name = name
        self.ip = ip
        self.mac = mac
        self.network = network

        # LAN connected to this interface
        self.lan = lan

        # Reference to parent router
        self.router = None

    def __str__(self):

        return (
            f"{self.name} | "
            f"IP: {self.ip} | "
            f"MAC: {self.mac}"
        )


# ============================================================
# ROUTER
# ============================================================

class Router:

    def __init__(self, name):

        self.name = name

        self.interfaces = []

        # List of:
        # (network, interface)
        self.routing_table = []

    # --------------------------------------------------------
    # ADD INTERFACE
    # --------------------------------------------------------

    def add_interface(self, interface, lan=None):

        # If LAN supplied here, associate it
        if lan is not None:

            interface.lan = lan

        # Store router reference
        interface.router = self

        self.interfaces.append(interface)

        # Add connected network to routing table
        self.routing_table.append(
            (
                interface.network,
                interface
            )
        )

        # Add router interface to LAN
        if interface.lan is not None:

            if interface not in interface.lan.devices:

                interface.lan.add_device(interface)

    # --------------------------------------------------------
    # GET INTERFACE BY IP
    # --------------------------------------------------------

    def get_interface_by_ip(self, ip):

        for interface in self.interfaces:

            if interface.ip == ip:

                return interface

        return None

    # --------------------------------------------------------
    # RECEIVE ARP REQUEST
    # --------------------------------------------------------

    def receive_arp_request(self, sender, target_ip):

        interface = self.get_interface_by_ip(target_ip)

        if interface is not None:

            print("\n[ROUTER ARP REPLY]")

            print(
                f"    Router Interface : "
                f"{interface.name}"
            )

            print(f"    IP               : {interface.ip}")
            print(f"    MAC              : {interface.mac}")
            print("    Delivery         : UNICAST")

            return interface.mac

        return None

    # --------------------------------------------------------
    # ROUTING TABLE LOOKUP
    # --------------------------------------------------------

    def route_packet(self, packet):

        destination = ipaddress.ip_address(
            packet.destination_ip
        )

        # Longest-prefix matching would be preferable
        # for a real router. For this simulator, the
        # routing table contains directly connected networks.

        for network, interface in self.routing_table:

            if destination in network:

                print("\n[ROUTING DECISION]")

                print(
                    f"    Destination : "
                    f"{packet.destination_ip}"
                )

                print(f"    Network     : {network}")

                print(
                    f"    Outbound IF : "
                    f"{interface.name}"
                )

                return interface

        print("\n[ROUTING FAILURE]")

        print(
            f"    No route to "
            f"{packet.destination_ip}"
        )

        return None

    # --------------------------------------------------------
    # RECEIVE PACKET
    # --------------------------------------------------------

    def receive_packet(
        self,
        packet,
        sender_mac,
        gateway_mac,
        incoming_lan
    ):

        print("\n" + "=" * 60)
        print(f"[ROUTER] {self.name} received Ethernet frame")

        print(f"    Source MAC      : {sender_mac}")
        print(f"    Destination MAC : {gateway_mac}")

        print("\n[IP PACKET INSIDE FRAME]")
        print(f"    Source IP      : {packet.source_ip}")
        print(f"    Destination IP : {packet.destination_ip}")
        print(f"    TTL            : {packet.ttl}")

        # Find which router interface received
        # the frame.
        incoming_interface = None

        for interface in self.interfaces:

            if (
                interface.mac == gateway_mac
                and interface.lan == incoming_lan
            ):

                incoming_interface = interface

                break

        if incoming_interface is None:

            print(
                "[ROUTER] Incoming interface "
                "could not be identified."
            )

            return

        print(
            f"[ROUTER] Incoming interface: "
            f"{incoming_interface.name}"
        )

        # Forward the IP packet
        self.forward_packet(packet)

    # --------------------------------------------------------
    # FORWARD PACKET
    # --------------------------------------------------------

    def forward_packet(self, packet):

        print("\n" + "=" * 60)
        print("[ROUTER] Processing IP packet")

        print(packet)

        # ----------------------------------------------------
        # 1. CHECK TTL
        # ----------------------------------------------------

        if packet.ttl <= 1:

            print("[ROUTER] TTL expired.")
            print("[ROUTER] Packet discarded.")

            return

        # ----------------------------------------------------
        # 2. DECREMENT TTL
        # ----------------------------------------------------

        packet.ttl -= 1

        print(
            f"[ROUTER] TTL decremented to "
            f"{packet.ttl}"
        )

        # ----------------------------------------------------
        # 3. ROUTING DECISION
        # ----------------------------------------------------

        outbound_interface = self.route_packet(packet)

        if outbound_interface is None:

            return

        # ----------------------------------------------------
        # 4. GET OUTBOUND LAN
        # ----------------------------------------------------

        outbound_lan = outbound_interface.lan

        if outbound_lan is None:

            print(
                "[ROUTER] Outbound interface "
                "is not connected to a LAN."
            )

            return

        print(
            f"\n[ROUTER] Outbound LAN: "
            f"{outbound_lan.name}"
        )

        # ----------------------------------------------------
        # 5. ARP ON OUTBOUND LAN
        # ----------------------------------------------------

        print(
            "\n[ROUTER] Performing ARP "
            "on outbound LAN"
        )

        destination_mac = (
            outbound_lan.handle_arp_request(
                outbound_interface,
                packet.destination_ip
            )
        )

        if destination_mac is None:

            print("[ROUTER] ARP failed.")
            print(
                "[ROUTER] Packet cannot be delivered."
            )

            return

        # ----------------------------------------------------
        # 6. CREATE NEW ETHERNET FRAME
        # ----------------------------------------------------

        print("\n[NEW ETHERNET FRAME]")

        print(
            f"    Source MAC       : "
            f"{outbound_interface.mac}"
        )

        print(
            f"    Destination MAC  : "
            f"{destination_mac}"
        )

        print(
            f"    Source IP        : "
            f"{packet.source_ip}"
        )

        print(
            f"    Destination IP   : "
            f"{packet.destination_ip}"
        )

        print(
            f"    TTL              : "
            f"{packet.ttl}"
        )

        # ----------------------------------------------------
        # 7. DELIVER PACKET
        # ----------------------------------------------------

        outbound_lan.deliver_packet(
            outbound_interface,
            destination_mac,
            packet.destination_ip,
            packet.data
        )
        
class RARPServer:
    def __init__(self, name, mac_ip_table):
        self.name = name
        self.mac_ip_table = mac_ip_table

    def receive_rarp_request(self, sender, mac):
        print(f"\n[RARP SERVER] {self.name} received RARP request")
        print(f"Requested MAC: {mac}")

        if mac in self.mac_ip_table:
            ip = self.mac_ip_table[mac]

            print(f"[RARP SERVER] MAC found!")
            print(f"[RARP SERVER] Sending RARP Reply:")
            print(f"    {mac} -> {ip}")

            sender.ip = ip

            print(f"[RARP] {sender.name} is now configured with IP {ip}")

        else:
            print(f"[RARP SERVER] MAC not found!")
            print(f"[RARP SERVER] No RARP Reply sent.")
            

if __name__ == "__main__":
    lan1 = LAN("LAN 1")
    lan2 = LAN("LAN 2")

    host_a = Host(
        "Host A",
        "AA:AA:AA:AA:AA:01",
        "192.168.1.10",
        "192.168.1.1"
    )

    host_b = Host(
        "Host B",
        "BB:BB:BB:BB:BB:01",
        "192.168.2.10",
        "192.168.2.1"
    )

    router = Router("R1")

    interface1 = RouterInterface(
        "R1-G0/0",
        "192.168.1.1",
        "AA:AA:AA:AA:AA:FF",
        ipaddress.ip_network("192.168.1.0/24"),
        lan1
    )

    interface2 = RouterInterface(
        "R1-G0/1",
        "192.168.2.1",
        "BB:BB:BB:BB:BB:FF",
        ipaddress.ip_network("192.168.2.0/24"),
        lan2
    )

    # Connect hosts
    lan1.add_device(host_a)
    lan2.add_device(host_b)

    # Connect router interfaces
    router.add_interface(interface1)
    router.add_interface(interface2)

    host_a.send_packet(
        "192.168.2.10",
        "Hello from Host A!",
        lan1
    )
    def test_rarp():

        print("\n")
        print("=" * 60)
        print("RARP TEST")
        print("=" * 60)

        # --------------------------------------------------------
        # RARP server database
        # --------------------------------------------------------

        rarp_table = {
            "AA:AA:AA:AA:AA:01": "192.168.1.10",
            "BB:BB:BB:BB:BB:01": "192.168.1.20"
        }

        # --------------------------------------------------------
        # Create RARP server
        # --------------------------------------------------------

        rarp_server = RARPServer(
            "RARP Server",
            rarp_table
        )

        # --------------------------------------------------------
        # Create host WITHOUT an IP address
        # --------------------------------------------------------

        host_a = Host(
            name="Host A",
            mac="AA:AA:AA:AA:AA:01",
            ip=None
        )

        print("\nBefore RARP:")
        print(f"    Host   : {host_a.name}")
        print(f"    MAC    : {host_a.mac}")
        print(f"    IP     : {host_a.ip}")

        # --------------------------------------------------------
        # Send RARP request
        # --------------------------------------------------------

        host_a.rarp_request(rarp_server)

        # --------------------------------------------------------
        # Check configuration
        # --------------------------------------------------------

        print("\nAfter RARP:")
        print(f"    Host   : {host_a.name}")
        print(f"    MAC    : {host_a.mac}")
        print(f"    IP     : {host_a.ip}")
        
        test_rarp()