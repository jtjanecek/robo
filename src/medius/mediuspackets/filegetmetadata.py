
from utils import utils

class FileGetMetaDataSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class FileGetMetaDataHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: FileGetMetaDataHandler')

