
from utils import utils

class MediusServerMoveGameWorldOnMeRequestSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class MediusServerMoveGameWorldOnMeRequestHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: MediusServerMoveGameWorldOnMeRequestHandler')

