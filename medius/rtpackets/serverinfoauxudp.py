from enums.enums import RtIdEnum, MediusEnum
from utils import utils

class ServerInfoAuxUdpSerializer:
	data_dict = [
		{'name': 'rtid', 'n_bytes': 1, 'cast': None},
		{'name': 'len', 'n_bytes': 2, 'cast': utils.bytes_to_int_little}
	]

	def serialize(self, data: bytes):
		raise Exception('Unimplemented Handler: ServerInfoAuxUdpSerializer')
		return utils.serialize(data, self.data_dict)

	@classmethod
	def build(self,
			ip,
			port
		):
		packet = [
			{'name': __name__},
			{'rtid': RtIdEnum.SERVER_INFO_AUX_UDP},
			{'ip': utils.str_to_bytes(ip, MediusEnum.BASIC_IP)},
			{"port": utils.int_to_bytes_little(2,port)}
		]
		return packet

class ServerInfoAuxUdpHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: ServerInfoAuxUdpHandler')

