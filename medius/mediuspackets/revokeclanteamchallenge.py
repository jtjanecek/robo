
from utils import utils

class RevokeClanTeamChallengeSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class RevokeClanTeamChallengeHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: RevokeClanTeamChallengeHandler')

