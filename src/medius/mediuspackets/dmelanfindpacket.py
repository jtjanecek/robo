
from utils import utils

class DMELANFindPacketSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class DMELANFindPacketHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: DMELANFindPacketHandler')

