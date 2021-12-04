from enums.enums import MediusIdEnum
from utils import utils

class GetLadderStatsWideResponseSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None}
    ]

    @classmethod
    def build(self,
            message_id,
            callback_status,
            account_or_clan_id,
            stats
        ):
        packet = [
            {'name': __name__},
            {'mediusid': MediusIdEnum.GetLadderStatsWideResponse},
            {'message_id': message_id},
            {'buf': utils.bytes_from_hex("000000")},
            {'callback_status': utils.int_to_bytes_little(4, callback_status)},
            {'account_or_clan_id': utils.int_to_bytes_little(4, account_or_clan_id)},
            {'stats': utils.bytes_from_hex(stats)}
        ]
        return packet

class GetLadderStatsWideResponseHandler:
    def process(self, serialized, monolith, con):
        raise Exception('Unimplemented Handler: GetLadderStatsWideResponseHandler')

