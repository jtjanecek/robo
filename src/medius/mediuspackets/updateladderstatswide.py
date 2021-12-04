from medius.mediuspackets.updateladderstatswideresponse import UpdateLadderStatsWideResponseSerializer
from utils import utils
from enums.enums import MediusEnum, CallbackStatus

class UpdateLadderStatsWideSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'buf', 'n_bytes': 3, 'cast': None},
        {'name': 'ladder_type', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'ladderstatswide', 'n_bytes': MediusEnum.LADDERSTATSWIDE_MAXLEN, 'cast': utils.bytes_to_hex}
    ]

class UpdateLadderStatsWideHandler:
    def process(self, serialized, monolith, con):
        client_manager = monolith.get_client_manager()

        account_id = client_manager.get_player_from_mls_con(con).get_account_id()

        client_manager.update_player_ladderstatswide(account_id, serialized['ladderstatswide'])

        return [UpdateLadderStatsWideResponseSerializer.build(
            serialized['message_id'],
            CallbackStatus.SUCCESS
        )]