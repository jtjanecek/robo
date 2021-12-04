
from utils import utils

class GetTotalChannelsSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class GetTotalChannelsHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GetTotalChannelsHandler')

