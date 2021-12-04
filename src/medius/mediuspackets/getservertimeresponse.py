
from utils import utils

class GetServerTimeResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class GetServerTimeResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GetServerTimeResponseHandler')

