
from utils import utils

class InvitePlayerToClanResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class InvitePlayerToClanResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: InvitePlayerToClanResponseHandler')

