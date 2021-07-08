
from utils import utils

class GetWorldSecurityLevelSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class GetWorldSecurityLevelHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: GetWorldSecurityLevelHandler')

