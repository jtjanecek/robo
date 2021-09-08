from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.gameinforesponse0 import GameInfoResponse0Serializer

class GameInfo0Serializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None},
		{'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
		{'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
		{'name': 'buf', 'n_bytes': 2, 'cast': None},
		{'name': 'dme_world_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little}
	]

class GameInfo0Handler:
	def process(self, serialized, monolith, con):

		game = monolith.get_client_manager().get_game(serialized['dme_world_id'])
		
		callback_status = CallbackStatus.SUCCESS

		if game == None:
			callback_status = CallbackStatus.GAME_NOT_FOUND
			return [GameInfoResponse0Serializer.build(
					serialized['message_id'],
					callback_status,
					0,
					0,
					0,
					0,
					0,
					0,
					utils.bytes_from_hex(''.join(['00'] * MediusEnum.GAMESTATS_MAXLEN)),
					utils.bytes_from_hex(''.join(['00'] * MediusEnum.GAMENAME_MAXLEN)),
					0,
					0,
					0,
					0,
					0,
					0
				)]

		created_info = game.get_created_info()

		return [GameInfoResponse0Serializer.build(
			serialized['message_id'],
			callback_status,
			created_info['app_id'],
			created_info['min_players'],
			created_info['max_players'],
			created_info['game_level'],
			created_info['player_skill_level'],
			game.get_player_count(),
			game.get_stats(),
			created_info['game_name'],
			created_info['rules_set'],
			created_info['generic_field_1'],
			created_info['generic_field_2'],
			created_info['generic_field_3'],
			game.get_game_status(),
			created_info['game_host_type']
		)]

