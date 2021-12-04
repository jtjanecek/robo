
from utils import utils

class RevokeClanInvitationSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class RevokeClanInvitationHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: RevokeClanInvitationHandler')

