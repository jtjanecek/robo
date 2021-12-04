
from utils import utils

class LadderPositionFastSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class LadderPositionFastHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: LadderPositionFastHandler')

