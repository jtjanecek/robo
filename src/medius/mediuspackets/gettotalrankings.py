
from utils import utils

class GetTotalRankingsSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class GetTotalRankingsHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GetTotalRankingsHandler')

