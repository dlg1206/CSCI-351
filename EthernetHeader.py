from Addresses import MACAddress
from IPv4Header import IPv4Header


class EthernetHeader:
    def __init__(self, hex_values: list[str]) -> None:
        self.destination_mac_address = MACAddress(hex_values[0:6])
        self.source_mac_address = MACAddress(hex_values[6:12])
        self.type = hex(int("".join(hex_values[12:14]), 16))
        self.ipv4_header = IPv4Header(hex_values[14:])

    def print(self) -> str:
        return (f"===== Ethernet Header =====\n"
                f"Destination Address:  {self.destination_mac_address}\n"
                f"Source Address:       {self.source_mac_address}\n"
                f"Type:                 {self.type}\n"
                f"{self.ipv4_header.print()}")
