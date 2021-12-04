
from utils import utils

class DMEServerVersionSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class DMEServerVersionHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: DMEServerVersionHandler')

