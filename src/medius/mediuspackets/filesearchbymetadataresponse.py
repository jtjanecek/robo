
from utils import utils

class FileSearchByMetaDataResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class FileSearchByMetaDataResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: FileSearchByMetaDataResponseHandler')

