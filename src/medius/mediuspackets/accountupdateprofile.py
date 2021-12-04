
from utils import utils

class AccountUpdateProfileSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class AccountUpdateProfileHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: AccountUpdateProfileHandler')

