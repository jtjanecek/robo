
from utils import utils

class CreateChannelResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class CreateChannelResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: CreateChannelResponseHandler')

