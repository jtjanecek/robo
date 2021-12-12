from enums.enums import MediusIdEnum
from utils import utils

class GetWorldSecurityLevelResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

    @classmethod
    def build(self,
            message_id: bytes,
            callback_status: int,
            world_id: int,
            app_type: int,
            security_level: int
            ):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.GetWorldSecurityLevelResponse},
            {'message_id': message_id},
            {'buf': utils.hex_to_bytes("000000")},
            {'callback_status': utils.int_to_bytes_little(4, callback_status)},
            {'world_id': utils.int_to_bytes_little(4, world_id)},
            {'app_type': utils.int_to_bytes_little(4, app_type)},
            {'security_level': utils.int_to_bytes_little(4, security_level)}
        ]
        return packet

class GetWorldSecurityLevelResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GetWorldSecurityLevelResponseHandler')