from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.ladderposition_extrainforesponse import LadderPosition_ExtraInfoResponseSerializer

class LadderPosition_ExtraInfoSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'buf', 'n_bytes': 3, 'cast': None},
        {'name': 'account_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'ladder_stat_index', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
    ]

class LadderPosition_ExtraInfoHandler:
    def process(self, serialized, monolith, con):

        player = monolith.get_client_manager().get_player_from_mls_con(con)
        player_account_id = player.get_account_id()
        username = player.get_username()

        rank = monolith.get_player_ranking(serialized['account_id'], serialized['ladder_stat_index'])

        stats = monolith.get_client_manager().get_player_stats(player_account_id)
        return [LadderPosition_ExtraInfoResponseSerializer.build(
                serialized['message_id'],
                CallbackStatus.SUCCESS,
                rank, # ladder position,
                99999, # total rankings,
        )]
        # return [LadderPosition_ExtraInfoResponseSerializer.build(
        #         serialized['message_id'],
        #         CallbackStatus.SUCCESS,
        #         1, # ladder position,
        #         1, # ladder stat,
        #         player_account_id, # account_id
        #         username, # username
        #         stats, # account stats
        #         0, # onlinestate1,
        #         0, # onlinestate2,
        #         0, # onlinestate3,
        #         "", # onlinestatelobbyname
        #         "", # onlinestategamename
        #         1 # endoflist
        #     )]
