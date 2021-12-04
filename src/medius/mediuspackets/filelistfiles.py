
from utils import utils

class FileListFilesSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class FileListFilesHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: FileListFilesHandler')

