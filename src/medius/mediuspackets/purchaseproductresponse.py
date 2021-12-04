
from utils import utils

class PurchaseProductResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class PurchaseProductResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: PurchaseProductResponseHandler')

