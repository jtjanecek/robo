from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.accountupdatestatsresponse import AccountUpdateStatsResponseSerializer

import logging
logger = logging.getLogger('robo.tests')

class AccountUpdateStatsSerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
        {'name': 'stats', 'n_bytes': MediusEnum.ACCOUNTSTATS_MAXLEN, 'cast': utils.bytes_to_hex}
    ]

class AccountUpdateStatsHandler:
    def process(self, serialized, monolith, con):
        client_manager = monolith.get_client_manager()

        player = client_manager.get_player_from_mls_con(con)
        player_account_id = player.get_account_id()

        client_manager.update_player_stats(player_account_id, serialized['stats'])

        updated_at = client_manager.get_player_stats(player_account_id)

        if serialized['stats'] != updated_at:
            logger.warning(f"Player stats did not get updated (account_id: {player_account_id})! Expected: {serialized['stats']}, actual: {updated_at}")

        return [AccountUpdateStatsResponseSerializer.build(
            serialized['message_id'],
            CallbackStatus.SUCCESS
        )]
