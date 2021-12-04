
from utils import utils

class CreateClanResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class CreateClanResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: CreateClanResponseHandler')

