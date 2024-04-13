"""
File: EthernetHeader.py
Description: Representation of an Ethernet Header

@author Derek Garcia
@contact dlg1206@rit.edu
"""

from Addresses import MACAddress
from IPv4Header import IPv4Header


class EthernetHeader:
    """
    Representation of an Ethernet Header
    """

    def __init__(self, hex_values: list[str]) -> None:
        """
        Create new Ethernet Header from provided hex values

        :param hex_values: Packet information as a list of hex values
        """
        self.destination_mac_address = MACAddress(hex_values[0:6])
        self.source_mac_address = MACAddress(hex_values[6:12])
        self.type = hex(int("".join(hex_values[12:14]), 16))
        self.ipv4_header = IPv4Header(hex_values[14:])  # pass next section of hex to child IPv4 header

    def print(self) -> str:
        """
        Pretty print Ethernet Header data

        :return: Formatted Ethernet Header data
        """
        return (f"=========== Ethernet Header ===========\n"
                f"Destination Address:  {self.destination_mac_address}\n"
                f"Source Address:       {self.source_mac_address}\n"
                f"Type:                 {self.type}\n"
                f"{self.ipv4_header.print()}")
