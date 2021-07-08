
from utils import utils

class VersionServerSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class VersionServerHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: VersionServerHandler')

