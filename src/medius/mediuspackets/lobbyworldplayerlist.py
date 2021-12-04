
from utils import utils

class LobbyWorldPlayerListSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class LobbyWorldPlayerListHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: LobbyWorldPlayerListHandler')

