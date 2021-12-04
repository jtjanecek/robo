
from utils import utils

class ModifyClanMessageResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class ModifyClanMessageResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: ModifyClanMessageResponseHandler')

