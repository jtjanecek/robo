
from utils import utils

class FileDownloadResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class FileDownloadResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: FileDownloadResponseHandler')

