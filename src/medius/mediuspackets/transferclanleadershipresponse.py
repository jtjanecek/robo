
from utils import utils

class TransferClanLeadershipResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class TransferClanLeadershipResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: TransferClanLeadershipResponseHandler')

