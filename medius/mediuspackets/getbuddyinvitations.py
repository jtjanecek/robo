
from utils import utils

class GetBuddyInvitationsSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class GetBuddyInvitationsHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: GetBuddyInvitationsHandler')

