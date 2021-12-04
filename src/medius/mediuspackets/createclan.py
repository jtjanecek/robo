
from utils import utils

class CreateClanSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class CreateClanHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: CreateClanHandler')

