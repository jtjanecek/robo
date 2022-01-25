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
        {'name': 'account_name', 'n_bytes': MediusEnum.PLAYERNAME_MAXLEN, 'cast': utils.bytes_to_str}
    ]

class FindPlayerHandler:
    def process(self, serialized, monolith, con):
        client_manager = monolith.get_client_manager()
        if serialized['account_id'] == 0:
            account_id = client_manager.get_account_id(username=serialized['account_name'])
        else:
            account_id = serialized['account_id']

        player = client_manager.get_player(account_id)

        app_type = MediusApplicationType.MEDIUS_APP_TYPE_GAME
        world_id = 0
        app_name = ''
        app_id = 0
        account_name = ''
        callback_status = CallbackStatus.NO_RESULT

        if player != None:
            account_name = player.get_username()
            status = player.get_player_status()
            callback_status = CallbackStatus.SUCCESS
            if status == MediusPlayerStatus.MEDIUS_PLAYER_IN_GAME_WORLD:
                world_id = player.get_game().get_dme_world_id()
            elif status == MediusPlayerStatus.MEDIUS_PLAYER_IN_CHAT_WORLD:
                world_id = player.get_mls_world_id()
                if world_id == 0:
                    world_id = client_manager.get_channels()[0]['id']
                app_type = MediusApplicationType.LOBBY_CHAT_CHANNEL

        return [FindPlayerResponseSerializer.build(
            serialized['message_id'],
            callback_status,
            app_id,
            app_name,
            app_type,
            world_id,
            account_id,
            account_name,
            1 # end of list
        )]
