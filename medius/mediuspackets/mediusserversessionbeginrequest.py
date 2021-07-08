
from utils import utils

class MediusServerSessionBeginRequestSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class MediusServerSessionBeginRequestHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: MediusServerSessionBeginRequestHandler')

