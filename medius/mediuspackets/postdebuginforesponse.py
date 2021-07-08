
from utils import utils

class PostDebugInfoResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class PostDebugInfoResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: PostDebugInfoResponseHandler')

