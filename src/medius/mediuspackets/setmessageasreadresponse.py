
from utils import utils

class SetMessageAsReadResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class SetMessageAsReadResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: SetMessageAsReadResponseHandler')

