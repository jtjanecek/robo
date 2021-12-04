
from utils import utils

class DMELANFindResultsPacketSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class DMELANFindResultsPacketHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: DMELANFindResultsPacketHandler')

