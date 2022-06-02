
import sys
sys.path.insert(0, '../../thug')
from medius.dme_serializer import TcpSerializer as tcp_map
from medius.dme_serializer import UdpSerializer as udp_map

from utils.utils import *


def blarg_filter(packet_type, src, dst, data_input: bytes) -> bytes:
    return data_input

    if src == 0:
        return data_input

    if packet_type == 'udp':
        return hex_to_bytes('0000')

    try:
        data = bytes_to_hex(data_input)

        # Convert to list. E.g. '000102030405' -> ['00', '01', '02', '03', '04', '05']
        data = deque([data[i:i+2] for i in range(0,len(data),2)])

        packets = []
        # Keep reading until data is empty
        while len(data) != 0:
            packet_id = data.popleft() + data.popleft() # E.g. '0201'
            # if packet_id in ['0209']:
            #     return hex_to_bytes('0000')
            #     return data_input
            if packet_type == 'tcp':
                serialized = tcp_map[packet_id].serialize(data)
            elif packet_type == 'udp':
                serialized = udp_map[packet_id].serialize(data)


            # if serialized.id not in [hex_to_bytes('0001'), hex_to_bytes('0213'), hex_to_bytes('0003'), hex_to_bytes('0018'), hex_to_bytes('0205'), hex_to_bytes('020C')]:
            #     packets.append(serialized)
            # if serialized.id not in [hex_to_bytes('020C')]:
            #     packets.append(serialized)
            if serialized.id == hex_to_bytes('020C') and serialized.subtype == 'p1_confirm':
                pass
            else:
                packets.append(serialized)

        for packet in packets:
            print(packet)

        data_new = b''
        for packet in packets:
            data_new += packet.to_bytes()

        return data_new
    except:
        print(bytes_to_hex(data_input))
        print("ERROR!")
        return data_input
