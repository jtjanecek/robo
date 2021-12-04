
from utils import utils

class RemovePlayerFromClanResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class RemovePlayerFromClanResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: RemovePlayerFromClanResponseHandler')

