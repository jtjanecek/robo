from enums.enums import MediusIdEnum
from enums.enums import MediusEnum
from utils import utils

class GetBuddyList_ExtraInfoResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

    @classmethod
    def build(self,
            message_id: bytes,
            template: str
            ):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.GetBuddyList_ExtraInfoResponse},
            {'message_id': message_id},
            {'TODO': utils.hex_to_bytes(template)}
        ]
        return packet

class GetBuddyList_ExtraInfoResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GetBuddyList_ExtraInfoResponseHandler')

