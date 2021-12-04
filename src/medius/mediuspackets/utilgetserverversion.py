
from utils import utils

class UtilGetServerVersionSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class UtilGetServerVersionHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: UtilGetServerVersionHandler')

