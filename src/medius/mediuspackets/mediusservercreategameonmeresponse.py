
from utils import utils

class MediusServerCreateGameOnMeResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class MediusServerCreateGameOnMeResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: MediusServerCreateGameOnMeResponseHandler')

