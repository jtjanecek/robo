
from utils import utils

class MediusServerCreateGameWithAttributesRequestSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class MediusServerCreateGameWithAttributesRequestHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: MediusServerCreateGameWithAttributesRequestHandler')

