
from utils import utils

class BanPlayerResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class BanPlayerResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: BanPlayerResponseHandler')

