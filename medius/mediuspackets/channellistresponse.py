
from utils import utils

class ChannelListResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class ChannelListResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: ChannelListResponseHandler')

