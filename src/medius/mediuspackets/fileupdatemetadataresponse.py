
from utils import utils

class FileUpdateMetaDataResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class FileUpdateMetaDataResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: FileUpdateMetaDataResponseHandler')

