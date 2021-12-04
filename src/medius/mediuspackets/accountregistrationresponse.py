
from utils import utils

class AccountRegistrationResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class AccountRegistrationResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: AccountRegistrationResponseHandler')

