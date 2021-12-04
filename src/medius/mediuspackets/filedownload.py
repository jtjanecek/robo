
from utils import utils

class FileDownloadSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class FileDownloadHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: FileDownloadHandler')

