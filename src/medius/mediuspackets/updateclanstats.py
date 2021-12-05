from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.updateclanstatsresponse import UpdateClanStatsResponseSerializer

class UpdateClanStatsSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
        {'name': 'buf', 'n_bytes': 2, 'cast': None},
        {'name': 'clan_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'stats', 'n_bytes': MediusEnum.CLANSTATS_MAXLEN, 'cast': None}
    ]

class UpdateClanStatsHandler:
    def process(self, serialized, monolith, con):

        stats = utils.bytes_to_hex(serialized['stats'])
        monolith.get_client_manager().update_clan_stats(serialized['clan_id'], stats)

        return [UpdateClanStatsResponseSerializer.build(
            serialized['message_id'],
            CallbackStatus.SUCCESS
        )]


