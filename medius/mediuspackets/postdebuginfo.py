
from utils import utils

class PostDebugInfoSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class PostDebugInfoHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: PostDebugInfoHandler')

