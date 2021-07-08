from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.creategameresponse import CreateGameResponseSerializer


class CreateGame1Serializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None},
		{'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
		{'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
		{'name': 'buf', 'n_bytes': 2, 'cast': None},
		{'name': 'app_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
		{'name': 'min_players', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
		{'name': 'max_players', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
		{'name': 'game_level', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
		{'name': 'game_name', 'n_bytes': MediusEnum.GAMENAME_MAXLEN, 'cast': None},
		{'name': 'game_password', 'n_bytes': MediusEnum.GAMEPASSWORD_MAXLEN, 'cast': None},
		{'name': 'spectator_password', 'n_bytes': MediusEnum.GAMEPASSWORD_MAXLEN, 'cast': None},
		{'name': 'player_skill_level', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
		{'name': 'rules_set', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
		{'name': 'generic_field_1', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
		{'name': 'generic_field_2', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
		{'name': 'generic_field_3', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
		{'name': 'game_host_type', 'n_bytes': 4, 'cast': utils.bytes_to_int_little}
	]

class CreateGame1Handler:
	def process(self, serialized, monolith, con):
		new_dme_world_id = monolith.get_client_manager().create_game(serialized)
		return [CreateGameResponseSerializer.build(
			serialized['message_id'],
			CallbackStatus.SUCCESS,
			new_dme_world_id
		)]