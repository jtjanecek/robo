
from utils import utils

class FileDeleteResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class FileDeleteResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: FileDeleteResponseHandler')

