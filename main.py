"""
File: main.py
Description: 

@author Derek Garcia
"""
import sys

from EthernetHeader import EthernetHeader

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


def valid_hex(hex_values: list[str]) -> bool:
    try:
        for hx in hex_values:
            int(hx, 16)
    except ValueError:
        return False
    return True


def main():
    with open(sys.argv[1]) as packet_file:
        for line in packet_file:
            # Skip if doesn't have byte string
            if line[0] != "|":
                continue
            # Clean hex values
            hex_values = line.strip().split("|")
            print(EthernetHeader(hex_values[2:-1]).print())     # pass only relevant hex


if __name__ == '__main__':
    main()
