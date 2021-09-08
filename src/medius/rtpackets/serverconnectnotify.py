from enums.enums import RtIdEnum
from utils import utils

class ServerConnectNotifySerializer:
	data_dict = [
		{'name': 'rtid', 'n_bytes': 1, 'cast': None},
		{'name': 'len', 'n_bytes': 2, 'cast': utils.bytes_to_int_little}
	]

	def serialize(self, data: bytes):
		raise Exception('Unimplemented Handler: ServerConnectNotifySerializer')
		return utils.serialize(data, self.data_dict)

	@classmethod
	def build(self,
			dme_player_id,
			ip):
		packet = [
			{'name': __name__},
			{'rtid': RtIdEnum.SERVER_CONNECT_NOTIFY},
			{"dme_player_id": utils.int_to_bytes_little(2,dme_player_id)},
			{"ip": utils.str_to_bytes(ip, 16)},
			{"buf": utils.bytes_from_hex("".join(["00"] * 64))}
		]
		return packet


class ServerConnectNotifyHandler:
	def process(self, serialized, monolith, con):
		raise Exception('Unimplemented Handler: ServerConnectNotifyHandler')

