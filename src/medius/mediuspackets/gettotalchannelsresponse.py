
from utils import utils

class GetTotalChannelsResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class GetTotalChannelsResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GetTotalChannelsResponseHandler')

