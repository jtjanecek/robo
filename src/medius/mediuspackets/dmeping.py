
from utils import utils

class DMEPingSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class DMEPingHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: DMEPingHandler')

