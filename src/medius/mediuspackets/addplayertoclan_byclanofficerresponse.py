
from utils import utils

class AddPlayerToClan_ByClanOfficerResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class AddPlayerToClan_ByClanOfficerResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: AddPlayerToClan_ByClanOfficerResponseHandler')

