
from utils import utils

class RevokeClanTeamChallengeResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class RevokeClanTeamChallengeResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: RevokeClanTeamChallengeResponseHandler')

