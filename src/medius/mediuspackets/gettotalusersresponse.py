
from utils import utils

class GetTotalUsersResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class GetTotalUsersResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GetTotalUsersResponseHandler')

