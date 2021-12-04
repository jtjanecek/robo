
from utils import utils

class FileDeleteSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class FileDeleteHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: FileDeleteHandler')

