
from utils import utils
from medius.rtpackets.serverconnectcomplete import ServerConnectCompleteSerializer

class ClientConnectReadyAuxUdpSerializer:
	data_dict = [
		{'name': 'rtid', 'n_bytes': 1, 'cast': None},
		{'name': 'len', 'n_bytes': 2, 'cast': utils.bytes_to_int_little}
	]

	def serialize(self, data: bytes):
		return utils.serialize(data, self.data_dict, __name__)

class ClientConnectReadyAuxUdpHandler:
	def process(self, serialized, monolith, con):
		return [ServerConnectCompleteSerializer.build()]
