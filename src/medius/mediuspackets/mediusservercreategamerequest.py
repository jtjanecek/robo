
from utils import utils

class MediusServerCreateGameRequestSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class MediusServerCreateGameRequestHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: MediusServerCreateGameRequestHandler')

