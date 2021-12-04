
from utils import utils

class AccountUpdateStats_OpenAccessSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class AccountUpdateStats_OpenAccessHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: AccountUpdateStats_OpenAccessHandler')

