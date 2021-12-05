from enums.enums import MediusIdEnum
from utils import utils
from enums.enums import MediusEnum, CallbackStatus

class CheckMyClanInvitationsResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

    @classmethod
    def build(self,
            message_id,
            callback_status
            ):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.CheckMyClanInvitationsResponse},
            {'message_id': message_id},
            {'buf': utils.bytes_from_hex("000000")},
            {'callback_status': utils.int_to_bytes_little(4, callback_status, signed=True)},
            {'clan_invitation_id': utils.int_to_bytes_little(4, 0)},
            {'clan_id': utils.int_to_bytes_little(4, 0)},
            {'response_status': utils.int_to_bytes_little(4, 0)},
            {'message': utils.str_to_bytes('', MediusEnum.CLANMSG_MAXLEN)},
            {'leader_account_id': utils.int_to_bytes_little(4, 0)},
            {'leader_account_name': utils.str_to_bytes('', MediusEnum.ACCOUNTNAME_MAXLEN)},
            {'end_of_list': utils.int_to_bytes_little(4, 1)},
        ]
        return packet

class CheckMyClanInvitationsResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: CheckMyClanInvitationsResponseHandler')

