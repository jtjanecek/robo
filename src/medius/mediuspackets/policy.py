from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.policyresponse import PolicyResponseSerializer

class PolicySerializer:
    data_dict = [
        {'name': 'mediusid', 'n_bytes': 2, 'cast': None},
        {'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None}
    ]

class PolicyHandler:
    def process(self, serialized, monolith, con):
        def chunks(s, n):
            """Produce `n`-character chunks from `s`."""
            res = []
            for start in range(0, len(s), n):
                res.append(s[start:start+n])
            return res
        policy = monolith.get_policy()

        packets = []
        policy_split = chunks(policy, MediusEnum.POLICY_MAXLEN-1)
        for i, policy_substr in enumerate(policy_split):
            end_of_list = int((i == (len(policy_split)-1)))
            packets.append(PolicyResponseSerializer.build(
                serialized['message_id'],
                CallbackStatus.SUCCESS,
                policy_substr,
                end_of_list
            ))


        player = monolith.get_client_manager().get_player_from_mls_con(con)
        if player is not None:
            monolith.process_login(player)

        return packets
