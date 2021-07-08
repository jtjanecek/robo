
from utils import utils

class JoinChannelFwdSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class JoinChannelFwdHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: JoinChannelFwdHandler')

