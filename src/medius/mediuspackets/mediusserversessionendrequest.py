
from utils import utils

class MediusServerSessionEndRequestSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class MediusServerSessionEndRequestHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: MediusServerSessionEndRequestHandler')

