
from utils import utils

class GameListResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class GameListResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GameListResponseHandler')

