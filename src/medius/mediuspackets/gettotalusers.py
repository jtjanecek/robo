
from utils import utils

class GetTotalUsersSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class GetTotalUsersHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GetTotalUsersHandler')

