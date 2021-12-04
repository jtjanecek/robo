
from utils import utils

class UniverseStatusList_ExtraInfoResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class UniverseStatusList_ExtraInfoResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: UniverseStatusList_ExtraInfoResponseHandler')

