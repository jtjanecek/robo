
from utils import utils

class GetClanInvitationsSentResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class GetClanInvitationsSentResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GetClanInvitationsSentResponseHandler')

