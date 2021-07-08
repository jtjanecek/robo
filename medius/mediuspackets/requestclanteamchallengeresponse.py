
from utils import utils

class RequestClanTeamChallengeResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class RequestClanTeamChallengeResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: RequestClanTeamChallengeResponseHandler')

