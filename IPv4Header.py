"""
File: IPv4Header.py
Description: Representation of an IPv4 Header

@author Derek Garcia
@contact dlg1206@rit.edu
"""

from enum import Enum

import Status
from Addresses import IPAddress
from Checksum import Checksum
from TCPHeader import TCPHeader


class FragmentFlag(Enum):
    """
    Utility Fragment Flag Enum
    """
    RESERVED = '0x0'
    DONT_FRAGMENT = '0x2'
    MORE_FRAGMENT = '0x1'


class IPv4Header:
    """
    Representation of an IPv4 Header
    """

    def __init__(self, hex_values: list[str]) -> None:
        """
        Create new IPv4 Header from provided hex values

        :param hex_values: Packet information as a list of hex values
        """
        self.checksum = Checksum(hex_values[0:20], 5)

        self.version = int(hex_values[0][0], 16)
        self.ihl = int(hex_values[0][1], 16)
        self.type_of_service = hex(int(hex_values[1], 16))
        self.total_length = int("".join(hex_values[2:4]), 16)
        self.identification = hex(int("".join(hex_values[4:6]), 16))

        # parse fragment
        fragment_details = parse_fragment("".join(hex_values[6:8]))
        self.flag = fragment_details[0]
        self.fragment_offset = fragment_details[1]

        self.ttl = int(hex_values[8], 16)
        self.protocol = int(hex_values[9], 16)
        self.header_checksum = self.checksum.get_checksum_value()
        self.source_ip_address = IPAddress(hex_values[12:16])
        self.destination_ip_address = IPAddress(hex_values[16:20])
        # Build TCP pseudo header
        pseudo_header = hex_values[12:20]  # src and dest ip
        pseudo_header.append("00")  # reserved bits
        pseudo_header.append(hex_values[9])  # protocol
        # calc TCP length and convert to hex
        tcp_len = "{:04x}".format(self.total_length - self.ihl * 4)
        pseudo_header.append(tcp_len[:2])
        pseudo_header.append(tcp_len[2:])
        self.tcp_header = TCPHeader(pseudo_header + hex_values[20:])  # pass next section of hex to child TCP header

    def print(self) -> str:
        """
        Pretty print IPv4 Header data

        :return: Formatted IPv4 Header data
        """
        calculated_checksum = self.checksum.calculate()
        return (f"============= IPv4 Header =============\n"
                f"Version:          {self.version}\n"
                f"IHL:              {self.ihl * 4} bytes ({self.ihl})\n"
                f"Type of Service:  {self.type_of_service}\n"
                f"Total Length:     {self.total_length}\n"
                f"Identification:   {self.ihl}\n"
                f"Control Flag:     {self.flag.name} ({self.flag.value})\n"
                f"Fragment Offset:  {self.fragment_offset}\n"
                f"TTL:              {self.ttl}\n"
                f"Protocol:         {self.protocol}\n"
                f"Header Checksum:  {self.header_checksum}\n"
                f"Source IP:        {self.source_ip_address}\n"
                f"Destination IP:   {self.destination_ip_address}\n"
                f"Valid Checksum:   {Status.valid() if calculated_checksum == self.header_checksum else Status.invalid()} (Calculated result: {calculated_checksum})\n"
                f"{self.tcp_header.print()}")  # pass next section of hex to child TCP header


def parse_fragment(hex_value: str) -> (FragmentFlag, int):
    """
    Parse fragment details from the give hex value

    :param hex_value: Hex value to interpret
    :return: (Fragment Flag, Fragment Offset)
    """
    # convert hex to bits and interpret
    bits = "{0:016b}".format(int(hex_value, 16), 'b')
    return FragmentFlag(hex(int(bits[0:3], 2))), int(bits[3:], 2)
