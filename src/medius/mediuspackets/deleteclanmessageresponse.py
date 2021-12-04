
from utils import utils

class DeleteClanMessageResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class DeleteClanMessageResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: DeleteClanMessageResponseHandler')

