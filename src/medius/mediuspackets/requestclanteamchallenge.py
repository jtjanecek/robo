
from utils import utils

class RequestClanTeamChallengeSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class RequestClanTeamChallengeHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: RequestClanTeamChallengeHandler')

