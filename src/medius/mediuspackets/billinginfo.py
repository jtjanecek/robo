
from utils import utils

class BillingInfoSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class BillingInfoHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: BillingInfoHandler')

