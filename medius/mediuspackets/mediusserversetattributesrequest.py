
from utils import utils

class MediusServerSetAttributesRequestSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class MediusServerSetAttributesRequestHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: MediusServerSetAttributesRequestHandler')

