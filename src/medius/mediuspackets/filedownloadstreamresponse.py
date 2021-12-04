
from utils import utils

class FileDownloadStreamResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class FileDownloadStreamResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: FileDownloadStreamResponseHandler')

