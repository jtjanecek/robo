from enums.enums import MediusEnum, CallbackStatus, MediusWorldStatus, MediusGameHostType, NetAddressType, NetConnectionType
from utils import utils
from medius.mediuspackets.joingameresponse import JoinGameResponseSerializer

class JoinGameSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None},
		{'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
		{'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
		{'name': 'buf', 'n_bytes': 2, 'cast': None},
		{'name': 'dme_world_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
		{'name': 'game_password', 'n_bytes': MediusEnum.GAMEPASSWORD_MAXLEN, 'cast': utils.bytes_to_str},
		{'name': 'game_host_type', 'n_bytes': 4, 'cast': utils.bytes_to_int_little}
	]

class JoinGameHandler:
	def process(self, serialized, monolith, con):

		client_manager = monolith.get_client_manager()
		game_status = client_manager.get_game_status(serialized['dme_world_id'])

		callback_status = CallbackStatus.SUCCESS
		if game_status in [MediusWorldStatus.WORLD_CLOSED, MediusWorldStatus.WORLD_INACTIVE, MediusWorldStatus.WORLD_ACTIVE]:
			callback_status = CallbackStatus.REQUEST_DENIED

		game_host_type = MediusGameHostType.HOST_CLIENT_SERVER_AUX_UDP

		net_connection_type = NetConnectionType.NET_CONNECTION_TYPE_CLIENT_SERVER_TCP_AUX_UDP

		dme_ip_type = NetAddressType.NET_ADDRESS_TYPE_EXTERNAL
		dmetcp_ip = monolith.get_dmetcp_ip()
		dmetcp_port = monolith.get_dmetcp_port()

		nat_ip_type = NetAddressType.NET_ADDRESS_TYPE_EXTERNAL
		nat_ip = monolith.get_nat_ip()
		nat_port = monolith.get_nat_port()

		encryption_key = utils.bytes_from_hex(''.join(['00'] * 64))
		session_key = serialized['session_key']
		access_key = client_manager.generate_access_key()

		if callback_status == CallbackStatus.REQUEST_DENIED:
			dmetcp_ip = ''
			nat_ip = ''


		return [JoinGameResponseSerializer.build(
			serialized['message_id'],
			callback_status,
			game_host_type,
			net_connection_type,
			dme_ip_type,
			dmetcp_ip,
			dmetcp_port,
			nat_ip_type,
			nat_ip,
			nat_port,
			serialized['dme_world_id'],
			encryption_key,
			session_key,
			access_key
		)] 