
from utils import utils

class UniverseVariableInformationResponseSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None}
	]

class UniverseVariableInformationResponseHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: UniverseVariableInformationResponseHandler')

