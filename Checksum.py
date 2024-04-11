"""
File: Checksum.py
Description: 

@author Derek Garcia
"""

SIXTEEN_BITS = 65535  # equivalent to 16 bits of 1


class Checksum:
    def __init__(self, hex_values: list[str], checksum_index: int):
        self.checksum_hex = [hex(int(hex_values[i] + hex_values[i + 1], 16)) for i in range(0, 20, 2)]
        self.checksum_index = checksum_index

    def get_checksum_value(self) -> hex:
        return self.checksum_hex[self.checksum_index]

    def validate(self) -> bool:
        check_sum = 0
        for i in range(0, len(self.checksum_hex)):
            # skip checksum index
            if i == self.checksum_index:
                continue
            # update total
            check_sum = check_sum + int(self.checksum_hex[i], 16)
            # carry 1 if > 16 bits
            if check_sum > SIXTEEN_BITS:
                bits = "{0:017b}".format(check_sum, 'b')
                check_sum = int(bits[1:], 2) + 1

        ones_comp = [str(int(bit) ^ 1) for bit in "{0:016b}".format(check_sum, 'b')]
        return "".join(ones_comp) == "{0:016b}".format(int(self.checksum_hex[self.checksum_index], 16), 'b')