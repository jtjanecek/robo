from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.channelinforesponse import ChannelInfoResponseSerializer

class ChannelInfoSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
        {'name': 'buf', 'n_bytes': 2, 'cast': None},
        {'name': 'world_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little}
    ]

class ChannelInfoHandler:
    def process(self, serialized, monolith, con):

        channels = monolith.get_client_manager().get_channels()
        lobby_name = None
        max_players = 0
        for channel in channels:
            if channel['id'] == serialized['world_id']:
                lobby_name = channel['lobby_name']
                max_players = channel['max_players']
                break

        if lobby_name == None:
            lobby_name = ''
            max_players = 8

        return [ChannelInfoResponseSerializer.build(
            serialized['message_id'],
            CallbackStatus.SUCCESS,
            lobby_name,
            0, # TODO: active player count
            max_players
        )]
