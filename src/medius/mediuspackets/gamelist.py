
from utils import utils

class GameListSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class GameListHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GameListHandler')

