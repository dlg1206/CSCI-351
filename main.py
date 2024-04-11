"""
File: main.py
Description: Main driver for processing packet files

@author Derek Garcia
"""
import os
import sys

import Status
from EthernetHeader import EthernetHeader
from Exception import validate_hex


def process_data(hex_values: list[str]) -> None:
    """
    Attempt to process packet data

    :param hex_values: List of hex values representing packet data
    """
    try:
        validate_hex(hex_values)
        print(EthernetHeader(hex_values).print())
    except Exception as e:
        print(f"Failed to process data | Reason: {e}", file=sys.stderr)


def main(packet_file_path: str) -> None:
    """
    Open packet file and process all packet data

    :param packet_file_path: Path to packet file
    """
    with open(packet_file_path) as packet_file:
        for line in packet_file:
            # Skip if doesn't have byte string
            if line[0] != "|":
                continue
            # Clean hex values
            hex_values = line.strip().split("|")
            process_data(hex_values[2:-1])  # pass only relevant hex


if __name__ == '__main__':
    try:
        # Check for file
        if len(sys.argv) < 2:
            raise Exception("Missing File Parameter")
        # assert file exists
        if not os.path.isfile(sys.argv[1]):
            raise Exception(f"File '{sys.argv[1]}' does not exist")
        # Launch the program
        main(sys.argv[1])
        exit(0)
    except Exception as e:
        print(f"{Status.Color.FAIL}Error: {e}{Status.Color.END}")
        print("Expected Usage: python3 main.py <path to packet file>")
        exit(1)
