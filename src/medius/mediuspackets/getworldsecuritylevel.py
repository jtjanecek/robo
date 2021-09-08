from enums.enums import MediusEnum, CallbackStatus, WorldSecurityLevelType
from utils import utils
from medius.mediuspackets.getworldsecuritylevelresponse import GetWorldSecurityLevelResponseSerializer

class GetWorldSecurityLevelSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None},
		{'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
		{'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
		{'name': 'buf', 'n_bytes': 2, 'cast': None},
		{'name': 'world_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
		{'name': 'app_type', 'n_bytes': 4, 'cast': utils.bytes_to_int_little}
	]

class GetWorldSecurityLevelHandler:
	def process(self, serialized, monolith, con):

		game = monolith.get_client_manager().get_game(serialized['world_id'])

		if game == None:
			return [GetWorldSecurityLevelResponseSerializer.build(
				serialized['message_id'],
				CallbackStatus.NO_RESULT,
				0,
				0,
				0
			)]
		return [GetWorldSecurityLevelResponseSerializer.build(
			serialized['message_id'],
			CallbackStatus.SUCCESS,
			serialized['world_id'],
			serialized['app_type'],
			WorldSecurityLevelType.WORLD_SECURITY_NONE # TODO: implement games with password protection
			)]