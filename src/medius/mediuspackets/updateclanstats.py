from enums.enums import MediusEnum, CallbackStatus, COLOR_MAP_1, CLANTAG_ALLOWED_CHARACTERS
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
        clan_stats = serialized['stats']

        clan_tag = serialized['stats'][16:24].hex().upper()
        ctag_valid, reason = utils.check_ctag_valid(clan_tag)
        if not ctag_valid:
            raise Exception(f'Invalid clan tag [{reason}]: {clan_tag}') # This will disconnect player

        client_manager = monolith.get_client_manager()
        clan_message = client_manager.get_clan_message(serialized['clan_id'])

        if clan_message == 'Colors 1':

            clan_tag = [clan_tag[i:i+4] for i in range(0,len(clan_tag),4)]
            for i in range(len(clan_tag)):
                character = CLANTAG_ALLOWED_CHARACTERS[clan_tag[i]]
                if character in COLOR_MAP_1.keys():
                    clan_tag[i] = COLOR_MAP_1[character]
            clan_tag = ''.join(clan_tag)
            clan_tag = utils.hex_to_bytes(clan_tag)
            clan_stats = bytearray(clan_stats)
            clan_stats[16:24] = clan_tag

        clan_stats = bytes(clan_stats)
        stats = utils.bytes_to_hex(clan_stats)
        monolith.get_client_manager().update_clan_stats(serialized['clan_id'], stats)

        return [UpdateClanStatsResponseSerializer.build(
            serialized['message_id'],
            CallbackStatus.SUCCESS
        )]


