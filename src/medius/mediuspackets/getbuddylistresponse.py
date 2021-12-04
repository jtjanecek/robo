
from utils import utils

class GetBuddyListResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class GetBuddyListResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GetBuddyListResponseHandler')

