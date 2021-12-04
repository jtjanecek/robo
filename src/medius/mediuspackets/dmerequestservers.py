
from utils import utils

class DMERequestServersSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class DMERequestServersHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: DMERequestServersHandler')

