
from utils import utils

class UpdateLadderStatsSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class UpdateLadderStatsHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: UpdateLadderStatsHandler')

