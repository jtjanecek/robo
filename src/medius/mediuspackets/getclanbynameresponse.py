from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from enums.enums import MediusIdEnum

class GetClanByNameResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

    @classmethod
    def build(self,
            message_id,
            callback_status,
            clan_id,
            leader_account_id,
            leader_account_name,
            stats,
            clan_status
        ):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.GetClanByNameResponse},
            {'message_id': message_id},
            {'buf': utils.hex_to_bytes("000000")},
            {'callback_status': utils.int_to_bytes_little(4, callback_status, signed=True)},
            {'clan_id': utils.int_to_bytes_little(4, clan_id)},
            {'leader_account_id': utils.int_to_bytes_little(4, leader_account_id)},
            {'leader_account_name': utils.str_to_bytes(leader_account_name, MediusEnum.ACCOUNTNAME_MAXLEN)},
            {'clan_stats': utils.hex_to_bytes(stats)},
            {'clan_status': utils.int_to_bytes_little(4, clan_status)}
        ]
        return packet

class GetClanByNameResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GetClanByNameResponseHandler')

