
from utils import utils

class GetUniverse_ExtraInfoSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class GetUniverse_ExtraInfoHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GetUniverse_ExtraInfoHandler')

