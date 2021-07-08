
from utils import utils

class GetClanTeamChallengesResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class GetClanTeamChallengesResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: GetClanTeamChallengesResponseHandler')

