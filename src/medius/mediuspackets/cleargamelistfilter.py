
from utils import utils

class ClearGameListFilterSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class ClearGameListFilterHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: ClearGameListFilterHandler')

