
from utils import utils

class BillingInfoResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class BillingInfoResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: BillingInfoResponseHandler')

