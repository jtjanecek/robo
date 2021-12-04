
from utils import utils

class MediusServerDisconnectPlayerRequestSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class MediusServerDisconnectPlayerRequestHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: MediusServerDisconnectPlayerRequestHandler')

