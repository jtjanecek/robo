
from utils import utils

class FileGetAttributesResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class FileGetAttributesResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: FileGetAttributesResponseHandler')

