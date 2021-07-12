from enums.enums import MediusEnum, MediusApplicationType, CallbackStatus, MediusPlayerStatus
from utils import utils
from medius.mediuspackets.findplayerresponse import FindPlayerResponseSerializer

class FindPlayerSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None},
		{'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
		{'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
		{'name': 'buf', 'n_bytes': 2, 'cast': None},
		{'name': 'search_type', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
		{'name': 'account_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
		{'name': 'account_name', 'n_bytes': MediusEnum.PLAYERNAME_MAXLEN, 'cast': None}
	]

class FindPlayerHandler:
	def process(self, serialized, monolith, con):
		player = monolith.get_client_manager().get_player(serialized['account_id'])

		app_type = MediusApplicationType.MEDIUS_APP_TYPE_GAME
		world_id = -1
		app_name = ''
		app_id = 0
		callback_status = CallbackStatus.NO_RESULT

		if player != None:
			status = player.get_player_status()
			callback_status = CallbackStatus.SUCCESS
			if status == MediusPlayerStatus.MEDIUS_PLAYER_IN_GAME_WORLD:
				world_id = player.get_game().get_dme_world_id()
			elif status == MediusPlayerStatus.MEDIUS_PLAYER_IN_CHAT_WORLD:
				world_id = player.get_mls_world_id()
				app_type = MediusApplicationType.LOBBY_CHAT_CHANNEL

		return [FindPlayerResponseSerializer.build(
			serialized['message_id'],
			callback_status,
			app_id,
			app_name,
			app_type,
			world_id,
			serialized['account_id'],
			serialized['account_name'],
			1 # end of list
		)]

