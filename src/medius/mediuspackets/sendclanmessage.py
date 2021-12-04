
from utils import utils

class SendClanMessageSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class SendClanMessageHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: SendClanMessageHandler')

