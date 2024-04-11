from enum import Enum

import Status
from Checksum import Checksum


class ControlFlag(Enum):
    CWR = 7
    ECE = 6
    URG = 5
    ACK = 4
    PSH = 3
    RST = 2
    SYN = 1
    FIN = 0


class ControlFlags:
    def __init__(self, bits: str):
        self.value = hex(int(bits, 2))
        self.flags = []
        # append flag if bit is on
        for i in range(0, 8):
            if bits[i] == '1':
                self.flags.append(ControlFlag(i))

    def print(self):
        return f"{self.value} ({', '.join([flag.name for flag in self.flags])})"



class TCPHeader:
    def __init__(self, hex_values: list[str]):
        # convert to hex vals for check sum
        self.checksum = Checksum(hex_values, 8)

        self.source_port = int("".join(hex_values[0:2]), 16)
        self.destination_port = int("".join(hex_values[2:4]), 16)
        self.sequence_number = int("".join(hex_values[4:8]), 16)
        self.acknowledgement_number = int("".join(hex_values[8:12]), 16)

        # parse control
        control_details = parse_control(hex_values[13])
        self.data_offset = control_details[0]
        self.reserved = control_details[1]
        self.control_flags = control_details[2]

        self.window = int("".join(hex_values[14:16]), 16)
        self.header_checksum = self.checksum.get_checksum_value()
        self.urgent_pointer = int("".join(hex_values[18:20]), 16)

    def print(self) -> str:
        return (f"============== TCP Header =============\n"
                f"Source Port:              {self.source_port}\n"
                f"Destination Port:         {self.destination_port}\n"
                f"Sequence Number:          {self.sequence_number}\n"
                f"Acknowledgement Number:   {self.acknowledgement_number}\n"
                f"Data Offset:              {self.data_offset}\n"
                f"Reserved:                 {self.reserved}\n"
                f"Control Flags:            {self.control_flags.print()}\n"
                f"Window:                   {self.window}\n"
                f"Checksum:                 {self.header_checksum}\n"
                f"Urgent Pointer:           {self.urgent_pointer}\n"
                f"Valid Checksum:           {Status.valid() if self.checksum.validate() else Status.invalid()}\n")


def parse_control(hex_value: str) -> (int, int, ControlFlags):
    # https://www.geeksforgeeks.org/python-ways-to-convert-hex-into-binary/
    # https://www.javatpoint.com/how-to-convert-hexadecimal-to-binary-in-python
    bits = "{0:016b}".format(int(hex_value, 16), 'b')
    return int(bits[0:4], 2), int(bits[4:8], 2), ControlFlags(bits[8:])
