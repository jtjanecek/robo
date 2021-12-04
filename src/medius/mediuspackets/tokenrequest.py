
from utils import utils

class TokenRequestSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class TokenRequestHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: TokenRequestHandler')

