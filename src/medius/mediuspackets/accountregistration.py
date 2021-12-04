
from utils import utils

class AccountRegistrationSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class AccountRegistrationHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: AccountRegistrationHandler')

