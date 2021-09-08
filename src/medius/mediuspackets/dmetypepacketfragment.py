
from utils import utils

class DMETypePacketFragmentSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class DMETypePacketFragmentHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: DMETypePacketFragmentHandler')

