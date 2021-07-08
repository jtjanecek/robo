
from utils import utils

class MediusServerAuthenticationResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class MediusServerAuthenticationResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: MediusServerAuthenticationResponseHandler')

