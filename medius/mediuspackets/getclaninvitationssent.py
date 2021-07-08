
from utils import utils

class GetClanInvitationsSentSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class GetClanInvitationsSentHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: GetClanInvitationsSentHandler')

