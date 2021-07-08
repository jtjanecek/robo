
from utils import utils

class WorldReport0Serializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class WorldReport0Handler:
	def process(self, serialized, monolith, con):
		return []