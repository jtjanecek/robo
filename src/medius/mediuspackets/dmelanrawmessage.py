
from utils import utils

class DMELANRawMessageSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class DMELANRawMessageHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: DMELANRawMessageHandler')

