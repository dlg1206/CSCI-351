"""
File: Addresses.py
Description: Utility classes to format MAC and IP addresses

@author Derek Garcia
@contact dlg1206@rit.edu
"""


class MACAddress:
    """
    Representation of a MAC Address
    """

    def __init__(self, hex_values: list[str]) -> None:
        """
        Create new MAC Address

        :param hex_values: Hex values that make up the MAC Address
        """
        self.address = list(hex_values[0:6])

    def __str__(self) -> str:
        """
        :return: MAC address string
        """
        # truncate parenthesis and replace commas and spaces with semicolons
        return f'{":".join(self.address)}'


class IPAddress:
    """
    Representation of an IP Address
    """

    def __init__(self, hex_values: list[str]) -> None:
        """
        Create new IP Address

        :param hex_values: Hex values that make up the IP Address
        """
        # Convert each hex value to base 10
        self.address = [int(hex_values[0], 16), int(hex_values[1], 16), int(hex_values[2], 16), int(hex_values[3], 16)]

    def __str__(self) -> str:
        """
        :return: IP Address String
        """
        # truncate parenthesis and replace commas and spaces with periods
        return f'{".".join(str(octet) for octet in self.address)}'
