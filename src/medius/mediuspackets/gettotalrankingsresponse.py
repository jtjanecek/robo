
from utils import utils

class GetTotalRankingsResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class GetTotalRankingsResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GetTotalRankingsResponseHandler')

