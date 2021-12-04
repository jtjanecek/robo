
from utils import utils

class MediusServerConnectGamesResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class MediusServerConnectGamesResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: MediusServerConnectGamesResponseHandler')

