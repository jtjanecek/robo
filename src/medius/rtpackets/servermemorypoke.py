from enums.enums import RtIdEnum
from utils import utils

class ServerMemoryPokeSerializer:
    data_dict = [
        {'name': 'rtid', 'n_bytes': 1, 'cast': None},
        {'name': 'len', 'n_bytes': 2, 'cast': utils.bytes_to_int_little}
    ]

    def serialize(self, data: bytes):
        raise Exception('Unimplemented Handler: ServerMemoryPokeSerializer')
        return utils.serialize(data, self.data_dict)

    @classmethod
    def build(self, address: int, payload: bytes):
        packet = [
            {'name': __name__},
            {'rtid': RtIdEnum.SERVER_MEMORY_POKE},
            {'address': utils.int_to_bytes_little(4, address)},
            {'count': utils.int_to_bytes_little(4, len(payload))},
            {'payload': payload}
        ]
        return packet

class ServerMemoryPokeHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: ServerMemoryPokeHandler')

