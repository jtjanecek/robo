from enums.enums import MediusEnum
from utils import utils
from infra.connection import UdpConnection
from medius.rtpackets.serverconnectacceptauxudp import ServerConnectAcceptAuxUdpSerializer

class ClientConnectAuxUdpSerializer:
	data_dict = [
		{'name': 'rtid', 'n_bytes': 1, 'cast': None},
		{'name': 'len', 'n_bytes': 2, 'cast': utils.bytes_to_int_little},
		{'name': 'buf', 'n_bytes': 3, 'cast': None},
		{'name': 'dme_world_id', 'n_bytes': 2, 'cast': utils.bytes_to_int_little},
		{'name': 'app_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
		{'name': 'ip', 'n_bytes': MediusEnum.BASIC_IP, 'cast': utils.bytes_to_str},
		{'name': 'port', 'n_bytes': MediusEnum.BASIC_PORT, 'cast': utils.bytes_to_int_little},
		{'name': 'dme_player_id', 'n_bytes': 2, 'cast': utils.bytes_to_int_little},
	]

	def serialize(self, data: bytes):
		return utils.serialize(data, self.data_dict, __name__)

class ClientConnectAuxUdpHandler:
	def process(self, serialized, monolith, con: UdpConnection):

		client_manager = monolith.get_client_manager()
		# tie this connection to the tcp connection

		client_manager.dmeudp_connected(con, serialized)

		return [ServerConnectAcceptAuxUdpSerializer.build(
			serialized['dme_player_id'],
			client_manager.get_dme_world_player_count(serialized['dme_world_id']),
			con.addr,
			con.port
		)]