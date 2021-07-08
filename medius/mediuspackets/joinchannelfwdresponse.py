
from utils import utils

class JoinChannelFwdResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class JoinChannelFwdResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: JoinChannelFwdResponseHandler')

