
from utils import utils

class GetClanMemberList_ExtraInfoSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class GetClanMemberList_ExtraInfoHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GetClanMemberList_ExtraInfoHandler')

