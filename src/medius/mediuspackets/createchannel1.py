
from utils import utils

class CreateChannel1Serializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class CreateChannel1Handler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: CreateChannel1Handler')

