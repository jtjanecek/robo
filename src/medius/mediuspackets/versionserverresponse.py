
from utils import utils

class VersionServerResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class VersionServerResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: VersionServerResponseHandler')

