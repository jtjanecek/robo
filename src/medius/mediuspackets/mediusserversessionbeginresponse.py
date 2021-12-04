
from utils import utils

class MediusServerSessionBeginResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class MediusServerSessionBeginResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: MediusServerSessionBeginResponseHandler')

