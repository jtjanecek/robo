
from utils import utils

class UpdateClanStatsResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class UpdateClanStatsResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: UpdateClanStatsResponseHandler')

