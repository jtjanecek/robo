
from utils import utils

class MediusServerEndGameRequestSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class MediusServerEndGameRequestHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: MediusServerEndGameRequestHandler')

