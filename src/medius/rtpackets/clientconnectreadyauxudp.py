
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

		# Get the player count
		player = monolith.get_client_manager().identify(con)

		game = player.get_game()

		player_count = game.get_player_count()

		game.send_server_notify_connected(player)

		return [ServerConnectCompleteSerializer.build(player_count=player_count)]
