
from utils import utils

class UtilAddGameWorldResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class UtilAddGameWorldResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: UtilAddGameWorldResponseHandler')

