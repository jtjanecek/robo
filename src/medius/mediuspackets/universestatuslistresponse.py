
from utils import utils

class UniverseStatusListResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class UniverseStatusListResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: UniverseStatusListResponseHandler')

