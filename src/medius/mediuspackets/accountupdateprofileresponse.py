
from utils import utils

class AccountUpdateProfileResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class AccountUpdateProfileResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: AccountUpdateProfileResponseHandler')

