
from utils import utils

class MediusServerCreateGameOnMeRequestSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class MediusServerCreateGameOnMeRequestHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: MediusServerCreateGameOnMeRequestHandler')

