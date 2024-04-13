"""
File: Checksum.py
Description: Utility for calculating checksums with provided hex values

@author Derek Garcia
@contact dlg1206@rit.edu
"""

SIXTEEN_BITS = 65535  # equivalent to 16 bits of 1


class Checksum:
    """
    Utility class for validating checksums
    """

    def __init__(self, hex_values: list[str], checksum_index: int) -> None:
        """
        Create a new Checksum

        :param hex_values: List of hex values that make up a packet
        :param checksum_index: index of the checksum value
        """
        # Convert to 10 hex values
        self.checksum_hex = [hex(int(hex_values[i] + hex_values[i + 1], 16)) for i in range(0, len(hex_values), 2)]
        self.checksum_index = checksum_index

    def get_checksum_value(self) -> hex:
        """
        :return: Checksum
        """
        return self.checksum_hex[self.checksum_index]

    def calculate(self) -> hex:
        """
        Calculate the checksum

        :return: Hex value of checksum
        """
        check_sum = 0
        for i in range(0, len(self.checksum_hex)):
            print(bin(check_sum)[2:])
            # skip checksum index
            if i == self.checksum_index:
                continue
            # update total
            check_sum = check_sum + int(self.checksum_hex[i], 16)
            # carry 1 if > 16 bits
            if check_sum > SIXTEEN_BITS:
                bits = "{0:017b}".format(check_sum, 'b')
                check_sum = int(bits[1:], 2) + 1

        # Flip bits to compute ones complement
        ones_comp = [str(int(bit) ^ 1) for bit in bin(check_sum)[2:]]
        return hex(int("".join(ones_comp), 2))
