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