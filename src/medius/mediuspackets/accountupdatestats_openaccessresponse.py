
from utils import utils

class AccountUpdateStats_OpenAccessResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class AccountUpdateStats_OpenAccessResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: AccountUpdateStats_OpenAccessResponseHandler')

