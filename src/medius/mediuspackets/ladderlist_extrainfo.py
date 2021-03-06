from enums.enums import MediusEnum, CallbackStatus, MediusWorldStatus, MediusGameHostType
from utils import utils
from medius.mediuspackets.ladderlist_extrainforesponse import LadderList_ExtraInfoResponseSerializer

class LadderList_ExtraInfoSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'buf', 'n_bytes': 3, 'cast': None},
        {'name': 'ladder_stat_index', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'sort_order', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'start_position', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'page_size', 'n_bytes': 4, 'cast': utils.bytes_to_int_little}
    ]

class LadderList_ExtraInfoHandler:
    def process(self, serialized, monolith, con):

        client_manager = monolith.get_client_manager()

        ladder_stat_index = serialized['ladder_stat_index']
        sort_order = 'ASC' if serialized['sort_order'] == 0 else 'DESC'
        start_position = serialized['start_position']
        end_position = start_position + serialized['page_size']

        accounts = monolith.get_leaderboard_info(ladder_stat_index, sort_order, start_position, end_position)


        rank = list(range(start_position, end_position))

        results = []
        for i, account in enumerate(accounts):
            results.append(LadderList_ExtraInfoResponseSerializer.build(
                serialized['message_id'],
                CallbackStatus.SUCCESS,
                rank[i],
                account['ladder_stats_wide'][ladder_stat_index], # ladder stat
                account['account_id'],
                account['username'],
                account['stats'],
                client_manager.get_player_status(account['account_id']),
                0, #lobby world id
                0, #game world id
                '', #lobbyname
                '', #game name
                int(i == (len(accounts)-1)) # end of list
            ))

        return results
