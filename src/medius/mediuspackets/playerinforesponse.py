from enums.enums import MediusIdEnum, MediusEnum
from utils import utils

class PlayerInfoResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

    @classmethod
    def build(self,
            message_id,
            callback_status,
            account_name,
            app_id,
            player_status,
            connection_class,
            stats
        ):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.PlayerInfoResponse},
            {'message_id': message_id},
            {'buf': utils.hex_to_bytes("000000")},
            {'callback_status': utils.int_to_bytes_little(4, callback_status)},
            {'account_name': utils.str_to_bytes(account_name, MediusEnum.ACCOUNTNAME_MAXLEN)},
            {'app_id': utils.int_to_bytes_little(4, app_id)},
            {'player_status': utils.int_to_bytes_little(4, player_status)},
            {'connection_class': utils.int_to_bytes_little(4, connection_class)},
            {'stats': utils.hex_to_bytes(stats)}
        ]
        return packet

class PlayerInfoResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: PlayerInfoResponseHandler')

