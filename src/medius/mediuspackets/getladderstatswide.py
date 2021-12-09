from medius.mediuspackets.getladderstatswideresponse import GetLadderStatsWideResponseSerializer
from utils import utils
from enums.enums import CallbackStatus, MediusEnum

class GetLadderStatsWideSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'buf', 'n_bytes': 3, 'cast': None},
        {'name': 'account_or_clan_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'ladder_type', 'n_bytes': 4, 'cast': utils.bytes_to_int_little}

    ]

class GetLadderStatsWideHandler:
    def process(self, serialized, monolith, con):


        client_manager = monolith.get_client_manager()

        if serialized['ladder_type'] == 0:
            ladderstatswide = client_manager.get_player_ladderstatswide(serialized['account_or_clan_id'])
        elif serialized['ladder_type'] == 1:
            ladderstatswide = client_manager.get_clan_statswide(serialized['account_or_clan_id'])
        else:
            raise Exception("Not implemented ladder type in GetLadderStatsWide!")

        #ladderstatswide = "3434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434"

        return [GetLadderStatsWideResponseSerializer.build(
                serialized['message_id'],
                CallbackStatus.SUCCESS,
                serialized['account_or_clan_id'],
                ladderstatswide
            )]
