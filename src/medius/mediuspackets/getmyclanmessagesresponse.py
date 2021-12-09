from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from enums.enums import MediusIdEnum

class GetMyClanMessagesResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
    ]

    @classmethod
    def build(self,
            message_id,
            callback_status,
            clan_id,
            message,
            end_of_list
            ):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.GetMyClanMessagesResponse},
            {'message_id': message_id},
            {'buf': utils.bytes_from_hex("000000")},
            {'callback_status': utils.int_to_bytes_little(4, callback_status, signed=True)},
            {'clan_id': utils.int_to_bytes_little(4, clan_id)},
            {'message': utils.str_to_bytes(message, MediusEnum.CLANMSG_MAXLEN)},
            {'end_of_list': utils.int_to_bytes_little(4, end_of_list)},
        ]
        return packet

class GetMyClanMessagesResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GetMyClanMessagesResponseHandler')

