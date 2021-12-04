
from utils import utils

class GetClanTeamChallengeHistoryResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

class GetClanTeamChallengeHistoryResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GetClanTeamChallengeHistoryResponseHandler')

