
from utils import utils

class CreateGameOnSelfSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class CreateGameOnSelfHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: CreateGameOnSelfHandler')

