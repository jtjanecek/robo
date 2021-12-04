
from utils import utils

class InvitePlayerToClanSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class InvitePlayerToClanHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: InvitePlayerToClanHandler')

