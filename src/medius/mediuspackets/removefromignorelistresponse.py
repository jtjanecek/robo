
from utils import utils

class RemoveFromIgnoreListResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class RemoveFromIgnoreListResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: RemoveFromIgnoreListResponseHandler')

