
from utils import utils

class MachineSignaturePostSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class MachineSignaturePostHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: MachineSignaturePostHandler')

