
from utils import utils

class FileUpdateMetaDataSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class FileUpdateMetaDataHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: FileUpdateMetaDataHandler')

