
from utils import utils

class BinaryMessageSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class BinaryMessageHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: BinaryMessageHandler')

