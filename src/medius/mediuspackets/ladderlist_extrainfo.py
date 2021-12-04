
from utils import utils

class LadderList_ExtraInfoSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class LadderList_ExtraInfoHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: LadderList_ExtraInfoHandler')

