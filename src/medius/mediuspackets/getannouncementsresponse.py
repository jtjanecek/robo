from enums.enums import MediusIdEnum
from enums.enums import MediusEnum
from utils import utils

class GetAnnouncementsResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

    @classmethod
    def build(self,
            message_id: bytes,
            callback_status: int,
            announcement_id: int,
            announcement: str,
            end_of_list: int
            ):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.GetAnnouncementsResponse},
            {'message_id': message_id},
            {'buf': utils.hex_to_bytes("000000")},
            {'callback_status': utils.int_to_bytes_little(4, callback_status)},
            {'announcement_id': utils.int_to_bytes_little(4, announcement_id)},
            {'announcement': utils.str_to_bytes(announcement, MediusEnum.ANNOUNCEMENT_MAXLEN)},
            {'end_of_list': utils.int_to_bytes_little(4, end_of_list)}
        ]
        return packet

class GetAnnouncementsResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GetAnnouncementsResponseHandler')


