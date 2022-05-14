from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.getannouncementsresponse import GetAnnouncementsResponseSerializer

class GetAllAnnouncementsSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None}
    ]


class GetAllAnnouncementsHandler:
    def process(self, serialized, monolith, con):
        #
        # player = monolith.get_client_manager().get_player_from_mls_con(con)
        # if player is not None:
        #     monolith.process_login(player)

        return [GetAnnouncementsResponseSerializer.build(
            serialized['message_id'],
            CallbackStatus.SUCCESS,
            1, # announcement id,
            monolith.get_announcement(),
            1, # end of list
        )]
