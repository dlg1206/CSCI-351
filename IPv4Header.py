from enum import Enum

from Addresses import IPAddress
from TCPHeader import TCPHeader

CHECKSUM_INDEX = {10, 11}


class FragmentFlag(Enum):
    RESERVED = '0x0'
    DONT_FRAGMENT = '0x2'
    MORE_FRAGMENT = '0x1'


class IPv4Header:

    def __init__(self, hex_values: list[str]):
        # convert to hex vals for check sum
        self.hex_values = [hex(int(hx, 16)) for hx in hex_values[0:20]]

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
        self.header_checksum = hex(int("".join(hex_values[10:12]), 16))
        self.source_ip_address = IPAddress(hex_values[12:16])
        self.destination_ip_address = IPAddress(hex_values[16:20])
        self.tcp_header = TCPHeader(hex_values[20:])

    def get_checksum_hex(self) -> list[hex]:
        checksum_hex = list(self.hex_values)
        for index in CHECKSUM_INDEX:
            checksum_hex[index] = '0x0'
        return checksum_hex


    def __str__(self) -> str:
        return (f"======= IPv4 Header =======\n"
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
                f"{self.tcp_header}")


def parse_fragment(hex_value: str) -> (FragmentFlag, int):
    # https://www.geeksforgeeks.org/python-ways-to-convert-hex-into-binary/
    # https://www.javatpoint.com/how-to-convert-hexadecimal-to-binary-in-python
    bits = "{0:016b}".format(int(hex_value, 16), 'b')

    return FragmentFlag(hex(int(bits[0:3], 2))), int(bits[3:], 2)
