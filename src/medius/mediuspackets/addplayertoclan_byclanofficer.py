
from utils import utils

class AddPlayerToClan_ByClanOfficerSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class AddPlayerToClan_ByClanOfficerHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: AddPlayerToClan_ByClanOfficerHandler')

