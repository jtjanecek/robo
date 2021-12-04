
from utils import utils

class GetBuddyInvitationsResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class GetBuddyInvitationsResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GetBuddyInvitationsResponseHandler')

