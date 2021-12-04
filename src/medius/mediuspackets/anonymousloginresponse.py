
from utils import utils

class AnonymousLoginResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class AnonymousLoginResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: AnonymousLoginResponseHandler')

