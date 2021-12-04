
from utils import utils

class GameList_ExtraInfoSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class GameList_ExtraInfoHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GameList_ExtraInfoHandler')

