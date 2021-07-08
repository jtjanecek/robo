
from utils import utils

class RespondToClanInvitationResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class RespondToClanInvitationResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: RespondToClanInvitationResponseHandler')

