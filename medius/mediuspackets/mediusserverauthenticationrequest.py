
from utils import utils

class MediusServerAuthenticationRequestSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class MediusServerAuthenticationRequestHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: MediusServerAuthenticationRequestHandler')

