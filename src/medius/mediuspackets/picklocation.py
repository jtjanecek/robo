
from utils import utils

class PickLocationSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class PickLocationHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: PickLocationHandler')

