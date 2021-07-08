from utils import utils
from enums.mediusid import MediusId
from medius.rtpackets.serverapp import ServerAppSerializer

class ClientAppToserverSerializer:
	data_dict = [
		{'name': 'rtid', 'n_bytes': 1, 'cast': None},
		{'name': 'len', 'n_bytes': 2, 'cast': utils.bytes_to_int_little},
		{'name': 'payload', 'n_bytes': None, 'cast': MediusId.serialize_medius_packet}
	]

	def serialize(self, data: bytes):
		return utils.serialize(data, self.data_dict, __name__)

class ClientAppToserverHandler:
	def process(self, serialized, monolith, con):

		# Pass the data to the medius handler
		medius_handler = MediusId.map[serialized['payload']['mediusid']]['handler']

		# Handle
		medius_packets = medius_handler.process(serialized['payload'], monolith, con)

		rt_packets = [ServerAppSerializer.build(medius_packet) for medius_packet in medius_packets]

		return rt_packets