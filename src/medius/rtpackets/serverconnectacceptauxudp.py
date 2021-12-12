from enums.enums import RtIdEnum
from utils import utils

class ServerConnectAcceptAuxUdpSerializer:
    data_dict = [
        {'name': 'rtid', 'n_bytes': 1, 'cast': None},
        {'name': 'len', 'n_bytes': 2, 'cast': utils.bytes_to_int_little}
    ]

    def serialize(self, data: bytes):
        raise Exception('Unimplemented Handler: ServerConnectAcceptAuxUdpSerializer')
        return utils.serialize(data, self.data_dict)

    @classmethod
    def build(self,
            dme_player_id,
            player_count,
            ipaddr,
            port):
        packet = [
            {'name': __name__},
            {'rtid': RtIdEnum.SERVER_CONNECT_ACCEPT_AUX_UDP},
            {'unknown': utils.hex_to_bytes("010810")},
            {"dme_player_id": utils.int_to_bytes_little(2,dme_player_id)},
            {"player_count": utils.int_to_bytes_little(2,player_count)},
            {'ip_addr': utils.pad_str(ipaddr,16).encode()},
            {"port": utils.int_to_bytes_little(2,port)}
        ]
        return packet

class ServerConnectAcceptAuxUdpHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: ServerConnectAcceptAuxUdpHandler')

