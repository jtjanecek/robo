from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from enums.enums import MediusIdEnum

class GetClanMemberList_ExtraInfoResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

    @classmethod
    def build(self,
            message_id,
            callback_status,
            account_id,
            account_name,
            account_stats,
            mediusPlayerOnlineStats,
            ladderstat,
            ladderposition,
            totalrankings,
            end_of_list
            ):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.GetClanMemberList_ExtraInfoResponse},
            {'message_id': message_id},
            {'buf': utils.bytes_from_hex("000000")},
            {'callback_status': utils.int_to_bytes_little(4, callback_status, signed=True)},
            {'account_id': utils.int_to_bytes_little(4, account_id)},
            {'account_name': utils.str_to_bytes(account_name, MediusEnum.ACCOUNTNAME_MAXLEN)},
            {'account_stats': utils.str_to_bytes(account_stats, MediusEnum.ACCOUNTSTATS_MAXLEN)},
            {'mediusPlayerOnlineStats': utils.int_to_bytes_little(4, mediusPlayerOnlineStats)},
            {'ladderstat': utils.int_to_bytes_little(4, ladderstat)},
            {'ladderposition': utils.int_to_bytes_little(4, ladderposition)},
            {'totalrankings': utils.int_to_bytes_little(4, totalrankings)},
            {'end_of_list': utils.int_to_bytes_little(4, end_of_list)},
        ]
        return packet


class GetClanMemberList_ExtraInfoResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GetClanMemberList_ExtraInfoResponseHandler')

