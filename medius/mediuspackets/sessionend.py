
from utils import utils

class SessionEndSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class SessionEndHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: SessionEndHandler')

