
from utils import utils

class CheckMyClanInvitationsResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class CheckMyClanInvitationsResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: CheckMyClanInvitationsResponseHandler')

