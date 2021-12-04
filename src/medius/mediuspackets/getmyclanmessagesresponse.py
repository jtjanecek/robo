
from utils import utils

class GetMyClanMessagesResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class GetMyClanMessagesResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GetMyClanMessagesResponseHandler')

