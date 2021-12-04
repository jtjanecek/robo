
from utils import utils

class UniverseNewsResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class UniverseNewsResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: UniverseNewsResponseHandler')

