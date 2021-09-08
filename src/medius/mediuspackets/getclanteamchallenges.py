
from utils import utils

class GetClanTeamChallengesSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class GetClanTeamChallengesHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: GetClanTeamChallengesHandler')

