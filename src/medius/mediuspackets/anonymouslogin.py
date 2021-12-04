
from utils import utils

class AnonymousLoginSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class AnonymousLoginHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: AnonymousLoginHandler')

