"""
File: Exception.py
Description: Collection of custom exceptions when parsing

@author Derek Garcia
"""

MIN_BYTES = 54  # Eth Header + IPv4 Header + TCP Header => 14 + 20 + 20 => 54


class InsufficientBytes(Exception):
    def __init__(self, num_bytes: int):
        """
        Not enough bytes to process all headers

        :param num_bytes: Number of bytes found
        """
        super().__init__(f"There must be at least 54 bytes to process header | Actual Bytes: {num_bytes}")


class InvalidHexValue(Exception):
    def __init__(self, invalid_hex: str):
        """
        Hex string is invalid hex

        :param invalid_hex: Invalid hex string
        """
        super().__init__(f"Failed to parse hex value | Invalid Hex Value: '{invalid_hex}'")


def validate_hex(hex_values: list[str]) -> None:
    """
    Validate list of hex values. Raise exception if failure

    :param hex_values: List of hex values to validate
    """
    # Not enough hex values for all headers
    if len(hex_values) < MIN_BYTES:
        raise InsufficientBytes(len(hex_values))

    # Ensure each hex value is valid hex
    for hx in hex_values:
        try:
            int(hx, 16)
        except ValueError:
            raise InvalidHexValue(hx)
