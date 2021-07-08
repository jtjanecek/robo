
from utils import utils

class ExtendedSessionBeginRequestSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class ExtendedSessionBeginRequestHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: ExtendedSessionBeginRequestHandler')

