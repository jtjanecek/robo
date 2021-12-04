
from utils import utils

class FileGetAttributesSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class FileGetAttributesHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: FileGetAttributesHandler')

