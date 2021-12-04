
from utils import utils

class MediusServerCreateGameWithAttributesResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class MediusServerCreateGameWithAttributesResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: MediusServerCreateGameWithAttributesResponseHandler')

