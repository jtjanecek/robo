
from utils import utils

class CreateGameOnSelfResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class CreateGameOnSelfResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: CreateGameOnSelfResponseHandler')

