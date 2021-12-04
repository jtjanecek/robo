
from utils import utils

class GenericChatSetFilterRequestSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class GenericChatSetFilterRequestHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GenericChatSetFilterRequestHandler')

