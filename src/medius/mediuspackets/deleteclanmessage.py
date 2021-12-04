
from utils import utils

class DeleteClanMessageSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class DeleteClanMessageHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: DeleteClanMessageHandler')

