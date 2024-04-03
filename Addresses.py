class MACAddress:
    def __init__(self, hex_values: list[str]):
        self.address = list(hex_values[0:6])

    def __str__(self) -> str:
        # truncate parenthesis and replace commas and spaces with semicolons
        return f'{":".join(self.address)}'


class IPAddress:
    def __init__(self, hex_values: list[str]) -> None:
        self.address = [int(hex_values[0], 16), int(hex_values[1], 16), int(hex_values[2], 16), int(hex_values[3], 16)]

    def __str__(self) -> str:
        # truncate parenthesis and replace commas and spaces with periods
        return f'{".".join(str(octet) for octet in self.address)}'
