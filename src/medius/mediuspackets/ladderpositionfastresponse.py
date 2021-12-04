
from utils import utils

class LadderPositionFastResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class LadderPositionFastResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: LadderPositionFastResponseHandler')

