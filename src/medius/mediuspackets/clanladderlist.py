from enums.enums import MediusEnum, CallbackStatus, MediusWorldStatus, MediusGameHostType
from utils import utils
from medius.mediuspackets.clanladderlistresponse import ClanLadderListResponseSerializer

class ClanLadderListSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'buf', 'n_bytes': 3, 'cast': None},
        {'name': 'ladder_stat_index', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'sort_order', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'start_position', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'page_size', 'n_bytes': 4, 'cast': utils.bytes_to_int_little}
    ]

class ClanLadderListHandler:
    def process(self, serialized, monolith, con):
        client_manager = monolith.get_client_manager()

        ladder_stat_index = serialized['ladder_stat_index']
        sort_order = 'ASC' if serialized['sort_order'] == 0 else 'DESC'
        start_position = serialized['start_position']
        end_position = start_position + serialized['page_size']

        clans = monolith.get_clan_leaderboard_info(ladder_stat_index, sort_order, start_position, end_position)

        rank = list(range(start_position, end_position))

        results = []
        for i, clan in enumerate(clans):
            results.append(ClanLadderListResponseSerializer.build(
                serialized['message_id'],
                clan['clan_id'],
                clan['clan_name'],
                rank[i],
                CallbackStatus.SUCCESS,
                int(i == (len(clans)-1)) # end of list
            ))

        return results
