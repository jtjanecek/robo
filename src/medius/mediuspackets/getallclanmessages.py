
from utils import utils

class GetAllClanMessagesSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class GetAllClanMessagesHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GetAllClanMessagesHandler')

