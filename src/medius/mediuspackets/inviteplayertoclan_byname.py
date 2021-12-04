
from utils import utils

class InvitePlayerToClan_ByNameSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class InvitePlayerToClan_ByNameHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: InvitePlayerToClan_ByNameHandler')

