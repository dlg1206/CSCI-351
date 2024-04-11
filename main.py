"""
File: main.py
Description: 

@author Derek Garcia
"""
import os
import sys

import Status
from EthernetHeader import EthernetHeader
from Exception import validate_bytes

BYTES_PER_HEX = 2


#
# Provide usage and/or operation messaging
# Process the Ethernet header fields - https://www.geeksforgeeks.org/ethernet-frame-format/
# Process the IP header fields - https://www.rfc-editor.org/rfc/rfc791#page-11
# Process the TCP header fields - https://www.rfc-editor.org/rfc/rfc9293#name-header-format
# Calculate the IP and TCP header checksum and compare them to the actual field values
# Document sources used in this program

# https://www.youtube.com/watch?v=7LniwyiH0SM
# https://www.thegeekstuff.com/2012/05/ip-header-checksum/


def process_data(hex_values: list[str]):
    try:
        validate_bytes(hex_values)
        print(EthernetHeader(hex_values).print())
    except Exception as e:
        print(f"Failed to process data | Reason: {e}", file=sys.stderr)


def main():
    with open(sys.argv[1]) as packet_file:
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
        main()
        exit(0)
    except Exception as e:
        print(f"{Status.Color.FAIL}Error: {e}{Status.Color.END}")
        print("Expected Usage: python3 main.py <path to packet file>")
        exit(1)
