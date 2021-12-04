
from utils import utils

class PurchaseProductRequestSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class PurchaseProductRequestHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: PurchaseProductRequestHandler')

