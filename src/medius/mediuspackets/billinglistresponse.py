
from utils import utils

class BillingListResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class BillingListResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: BillingListResponseHandler')

