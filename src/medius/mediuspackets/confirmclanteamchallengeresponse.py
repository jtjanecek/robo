
from utils import utils

class ConfirmClanTeamChallengeResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class ConfirmClanTeamChallengeResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: ConfirmClanTeamChallengeResponseHandler')

