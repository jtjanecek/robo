
from utils import utils

class GetLadderStatsSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class GetLadderStatsHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GetLadderStatsHandler')

