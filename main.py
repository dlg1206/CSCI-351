"""
File: main.py
Description: 

@author Derek Garcia
"""
from EthernetHeader import EthernetHeader
from IPv4Header import IPv4Header
from TCPHeader import TCPHeader

BYTES_PER_HEX = 2


#
# Provide usage and/or operation messaging
# Process the Ethernet header fields - https://www.geeksforgeeks.org/ethernet-frame-format/
# Process the IP header fields - https://www.rfc-editor.org/rfc/rfc791#page-11
# Process the TCP header fields - https://www.rfc-editor.org/rfc/rfc9293#name-header-format
# Calculate the IP and TCP header checksum and compare them to the actual field values
# Document sources used in this program

# class EthernetHeader:
#     def __int__(self, ):
# https://www.youtube.com/watch?v=7LniwyiH0SM
# https://www.thegeekstuff.com/2012/05/ip-header-checksum/

def validate_checksum(header: IPv4Header | TCPHeader) -> bool:
    checksum_hex = header.checksum_hex
    # checksum_hex = ["0x4500", "0x003c", "0x1c46", "0x4000", "0x4006", "0xb1e6", "0xac10", "0x0a63", "0xac10", "0x0a0c" ]
    check_sum = 0
    while len(checksum_hex) != 0:
        val = int(checksum_hex.pop(0), 16)
        if val == int(header.header_checksum, 16):
        # if val == int("0xb1e6", 16):
            continue
        check_sum = check_sum + val
        if check_sum > 65535:
            bits = "{0:017b}".format(check_sum, 'b')
            carry = " {0:016b}".format(int(bits[1:], 2) + 1, 'b')
            print(f"\t{bits}")
            print(f"\t{carry}")
            check_sum = int(bits[1:], 2) + 1
        # print("{0:016b}".format(check_sum, 'b'))
        print(hex(check_sum))
    ones_comp = [str(int(bit) ^ 1) for bit in "{0:016b}".format(check_sum, 'b')]
    print(f"result:         {"{0:016b}".format(check_sum, 'b')}")
    print(f"ones comp:      {''.join(ones_comp)}")
    # print(f"ones comp: {int(''.join(ones_comp), 2)}")
    print(f"checksum hex:   {"{0:016b}".format(int(header.header_checksum, 16), 'b')}")
    # print(f"checksum:       {"{0:016b}".format(int("0xb1e6", 16), 'b')}")
    var = 1


def valid_hex(hex_values: list[str]) -> bool:
    try:
        for hx in hex_values:
            int(hx, 16)
    except ValueError:
        return False
    return True


# ===== Ethernet Header =====
# ======== TCP Header =======
# ======= IPv4 Header =======

if __name__ == '__main__':
    # print(hex_to_ip(('0a', 'd2', 'c8', '6f')))
    list = ("00|05|0d|ce|90|78|00|50|ba|c4|2e|04|08|00|45|00|00|28|2f|c1|40|00|80|06|24|8b|0a|d2|c8|6f|0a|d2|c8|70|13"
            "|c4|13|c4|d7|49|7c|f2|c7|b9|30|b4|50|10|fb|d3|99|4a|00|00|20|20|20|20|20|20").split("|")
    i = EthernetHeader(list)
    validate_checksum(i.ipv4_header)
    print(i.print())
    # with open("in/tcp-2.txt") as f:
    #     val = f.readline().strip().replace(" ", "")[1:-1].split("|")
    #
    # print(valid_hex(val))
