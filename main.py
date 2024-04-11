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
    # list = ("00|00|5e|00|01|01|c8|34|8e|63|5b|6b|08|00|45|00|00|6c|74|81|40|00|80|06|00|00|81|15|88|d5|42|18|dc|78|ec|fa|04|aa|15|1f|33|98|24|a3|f2|bf|50|18|03|fe|28|da|00|00|00|42|48|00|00|00|00|01|4d|a6|37|94|e6|a5|04|8c|10|c0|cc|cd|40|9d|b2|9a|0a|5e|5e|26|d3|1a|dd|73|e5|e7|da|c1|d0|12|9b|2d|e0|3e|8a|32|83|b4|68|8f|4c|39|9f|31|93|4a|3e|0e|a2|79|ab|f1|f9|d1|2a|ef|ea|d9|1c|52").split("|")
    i = EthernetHeader(list)
    print(i.print())
    # with open("in/tcp-2.txt") as f:
    #     val = f.readline().strip().replace(" ", "")[1:-1].split("|")
    #
    # print(valid_hex(val))
