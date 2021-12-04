
from utils import utils

class GetClanMemberListResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class GetClanMemberListResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GetClanMemberListResponseHandler')

