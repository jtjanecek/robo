
from utils import utils

class FileListFilesResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class FileListFilesResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: FileListFilesResponseHandler')

