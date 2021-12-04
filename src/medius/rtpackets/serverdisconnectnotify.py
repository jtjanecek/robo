from enums.enums import RtIdEnum
from utils import utils

class ServerDisconnectNotifySerializer:
    data_dict = [
        {'name': 'rtid', 'n_bytes': 1, 'cast': None},
        {'name': 'len', 'n_bytes': 2, 'cast': utils.bytes_to_int_little}
    ]

    @classmethod
    def build(self,
            dme_player_id,
            ip):
        packet = [
            {'name': __name__},
            {'rtid': RtIdEnum.SERVER_DISCONNECT_NOTIFY},
            {"dme_player_id": utils.int_to_bytes_little(2,dme_player_id)},
            {"ip": utils.str_to_bytes(ip, 16)}
        ]
        return packet

    def serialize(self, data: bytes):
        raise Exception('Unimplemented Handler: ServerDisconnectNotifySerializer')
        return utils.serialize(data, self.data_dict)

class ServerDisconnectNotifyHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: ServerDisconnectNotifyHandler')

