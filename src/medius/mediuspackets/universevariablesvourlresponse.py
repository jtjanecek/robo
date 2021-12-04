
from utils import utils

class UniverseVariableSvoURLResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class UniverseVariableSvoURLResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: UniverseVariableSvoURLResponseHandler')

