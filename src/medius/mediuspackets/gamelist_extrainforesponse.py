
from utils import utils

class GameList_ExtraInfoResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class GameList_ExtraInfoResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GameList_ExtraInfoResponseHandler')

