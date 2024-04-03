from enum import Enum

CHECKSUM_INDEX = {16, 17}

class ControlFlag(Enum):
    CWR = '0x80'
    ECE = '0x40'
    URG = '0x20'
    ACK = '0x10'
    PSH = '0x08'
    RST = '0x04'
    SYN = '0x02'
    FIN = '0x01'


class TCPHeader:
    def __init__(self, hex_values: list[str]):
        # convert to hex vals for check sum
        self.hex_values = [hex(int(hx, 16)) for hx in hex_values[0:20]]

        self.source_port = int("".join(hex_values[0:2]), 16)
        self.destination_port = int("".join(hex_values[2:4]), 16)
        self.sequence_number = int("".join(hex_values[4:8]), 16)
        self.acknowledgement_number = int("".join(hex_values[8:12]), 16)

        # parse control
        control_details = parse_control(hex_values[13])
        self.data_offset = control_details[0]
        self.reserved = control_details[1]
        self.control_flag = control_details[2]

        self.window = int("".join(hex_values[14:16]), 16)
        self.checksum = hex(int("".join(hex_values[16:18]), 16))
        self.urgent_pointer = int("".join(hex_values[18:20]), 16)

    def __str__(self) -> str:
        return (f"======== TCP Header =======\n"
                f"Source Port:              {self.source_port}\n"
                f"Destination Port:         {self.destination_port}\n"
                f"Sequence Number:          {self.sequence_number}\n"
                f"Acknowledgement Number:   {self.acknowledgement_number}\n"
                f"Data Offset:              {self.data_offset}\n"
                f"Reserved:                 {self.reserved}\n"
                f"Control Flag:             {self.control_flag.name} ({self.control_flag.value})\n"
                f"Window:                   {self.window}\n"
                f"Checksum:                 {self.checksum}\n"
                f"Urgent Pointer:           {self.urgent_pointer}")


def parse_control(hex_value: str) -> (int, int, ControlFlag):
    # https://www.geeksforgeeks.org/python-ways-to-convert-hex-into-binary/
    # https://www.javatpoint.com/how-to-convert-hexadecimal-to-binary-in-python
    bits = "{0:016b}".format(int(hex_value, 16), 'b')
    return int(bits[0:4], 2), int(bits[4:8], 2), ControlFlag(hex(int(bits[8:], 2)))
