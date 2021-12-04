
from utils import utils

class TransferClanLeadershipSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class TransferClanLeadershipHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: TransferClanLeadershipHandler')

