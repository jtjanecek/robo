
from utils import utils

class UpdateClanStatsSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class UpdateClanStatsHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: UpdateClanStatsHandler')

