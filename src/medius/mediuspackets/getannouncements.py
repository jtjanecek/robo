
from utils import utils

class GetAnnouncementsSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class GetAnnouncementsHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GetAnnouncementsHandler')

