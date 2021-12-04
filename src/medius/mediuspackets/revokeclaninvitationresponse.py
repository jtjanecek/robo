
from utils import utils

class RevokeClanInvitationResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class RevokeClanInvitationResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: RevokeClanInvitationResponseHandler')

