
from utils import utils

class DMEClientConnectsSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class DMEClientConnectsHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: DMEClientConnectsHandler')

