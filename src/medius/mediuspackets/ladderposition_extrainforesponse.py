from enums.enums import MediusIdEnum, MediusEnum
from utils import utils

class LadderPosition_ExtraInfoResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

    @classmethod
    def build(self,
            message_id: bytes,
            callback_status: int,
            ladder_position: int,
            ladder_stat: int,
            account_id: int,
            username: str,
            account_stats: str,
            onlinestate1: int,
            onlinestate2: int,
            onlinestate3: int,
            onlinestatelobbyname: str,
            onlinestategamename: str,
            endoflist: int
            ):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.LadderPosition_ExtraInfoResponse},
            {'message_id': message_id},
            {'buf': utils.bytes_from_hex("000000")},
            {'ladder_position': utils.int_to_bytes_little(4, ladder_position)},
            {'ladder_stat': utils.int_to_bytes_little(4, ladder_stat)},
            {'account_id': utils.int_to_bytes_little(4, account_id)},
            {'username': utils.str_to_bytes(username, MediusEnum.ACCOUNTNAME_MAXLEN)},
            {'account_stats': utils.str_to_bytes(username, MediusEnum.ACCOUNTSTATS_MAXLEN)},
            {'onlinestate1': utils.int_to_bytes_little(4, onlinestate1)},
            {'onlinestate2': utils.int_to_bytes_little(4, onlinestate2)},
            {'onlinestate3': utils.int_to_bytes_little(4, onlinestate3)},
            {'onlinestatelobbyname': utils.str_to_bytes(onlinestatelobbyname, MediusEnum.WORLDNAME_MAXLEN)},
            {'onlinestategamename': utils.str_to_bytes(onlinestategamename, MediusEnum.WORLDNAME_MAXLEN)},
            {'endoflist': utils.int_to_bytes_little(4, endoflist)}
        ]
        return packet

class LadderPosition_ExtraInfoResponseHandler:
    def process(self, serialized, monolith, con):
        pass