"""
File: Exception.py
Description: 

@author Derek Garcia
"""

MIN_BYTES = 54


class InsufficientBytes(Exception):
    def __init__(self, num_bytes: int):
        super().__init__(f"There must be at least 54 bytes to process header | Actual Bytes: {num_bytes}")


class InvalidHexValue(Exception):
    def __init__(self, invalid_hex: str):
        super().__init__(f"Failed to parse hex value | Invalid Hex Value: '{invalid_hex}'")

class MissingArgument(Exception):
    def __init__(self):
        super().__init__("Missing file parameter")

def validate_bytes(hex_values: list[str]):
    if len(hex_values) < MIN_BYTES:
        raise InsufficientBytes(len(hex_values))

    for hx in hex_values:
        try:
            int(hx, 16)
        except ValueError:
            raise InvalidHexValue(hx)
