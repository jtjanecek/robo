
from utils import utils

class DnasSignaturePostSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class DnasSignaturePostHandler:
	def process(self, serialized, monolith, con):
		return []

