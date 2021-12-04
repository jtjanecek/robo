
from utils import utils

class VoteToBanPlayerRequestSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class VoteToBanPlayerRequestHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: VoteToBanPlayerRequestHandler')

