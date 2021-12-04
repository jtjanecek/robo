
from utils import utils

class BillingTunnelRequestSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class BillingTunnelRequestHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: BillingTunnelRequestHandler')

