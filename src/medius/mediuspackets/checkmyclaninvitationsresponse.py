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
            callback_status,
            clan_invitation_id = 0,
            clan_id = 0,
            response_status = 0,
            message = '',
            leader_account_id = 0,
            leader_account_name = '',
            end_of_list = 1
              ):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.CheckMyClanInvitationsResponse},
            {'message_id': message_id},
            {'buf': utils.hex_to_bytes("000000")},
            {'callback_status': utils.int_to_bytes_little(4, callback_status, signed=True)},
            {'clan_invitation_id': utils.int_to_bytes_little(4, clan_invitation_id)},
            {'clan_id': utils.int_to_bytes_little(4, clan_id)},
            {'response_status': utils.int_to_bytes_little(4, response_status)},
            {'message': utils.str_to_bytes(message, MediusEnum.CLANMSG_MAXLEN)},
            {'leader_account_id': utils.int_to_bytes_little(4, leader_account_id)},
            {'leader_account_name': utils.str_to_bytes(leader_account_name, MediusEnum.ACCOUNTNAME_MAXLEN)},
            {'end_of_list': utils.int_to_bytes_little(4, end_of_list)},
        ]
        return packet

class CheckMyClanInvitationsResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: CheckMyClanInvitationsResponseHandler')

