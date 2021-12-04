
from utils import utils

class FileGetMetaDataResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class FileGetMetaDataResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: FileGetMetaDataResponseHandler')

