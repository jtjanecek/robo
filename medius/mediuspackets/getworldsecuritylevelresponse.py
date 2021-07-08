
from utils import utils

class GetWorldSecurityLevelResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class GetWorldSecurityLevelResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: GetWorldSecurityLevelResponseHandler')

