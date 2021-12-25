from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.createchannelresponse import CreateChannelResponseSerializer

class CreateChannelSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
        {'name': 'buf', 'n_bytes': 2, 'cast': None},
        {'name': 'app_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'max_players', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'game_level', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'lobby_name', 'n_bytes': MediusEnum.LOBBYNAME_MAXLEN, 'cast': utils.bytes_to_str},
        {'name': 'lobby_password', 'n_bytes': MediusEnum.GAMEPASSWORD_MAXLEN, 'cast': None},
        {'name': 'generic_field_1', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'generic_field_2', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'generic_field_3', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'generic_field_4', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'generic_field_level', 'n_bytes': 4, 'cast': utils.bytes_to_int_little}
    ]

class CreateChannelHandler:
    def process(self, serialized, monolith, con):

        new_world_id = monolith.get_client_manager().create_channel(serialized)

        return [CreateChannelResponseSerializer.build(
            serialized['message_id'],
            CallbackStatus.SUCCESS,
            new_world_id
        )]
