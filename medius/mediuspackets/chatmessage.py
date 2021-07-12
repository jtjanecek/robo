from enums.enums import MediusEnum, MediusChatMessageType, RtIdEnum
from utils import utils
from medius.mediuspackets.chatfwdmessage import ChatFwdMessageSerializer

class ChatMessageSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None},
		{'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
		{'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
		{'name': 'buf', 'n_bytes': 2, 'cast': None},
		{'name': 'chat_message_type', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
		{'name': 'target_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
		{'name': 'text', 'n_bytes': MediusEnum.CHATMESSAGE_MAXLEN, 'cast': None}
	]

class ChatMessageHandler:
	def process(self, serialized, monolith, con):
		player = monolith.get_client_manager().get_player_from_mls_con(con)

		mls_world_id = player.get_mls_world_id()

		packet = [{'name': 'Server app'}, {'rtid': RtIdEnum.SERVER_APP}]
		packet.append({'payload':ChatFwdMessageSerializer.build(serialized['message_id'], player.get_account_id(), player.get_username(), serialized['chat_message_type'], serialized['text'])})
		packet = utils.rtpacket_to_bytes(packet)

		if serialized['chat_message_type'] == MediusChatMessageType.BROADCAST:
			for dst_player in monolith.get_client_manager().get_players_by_world(mls_world_id):
				if player != dst_player:
					dst_player.send_mls(packet)
		elif serialized['chat_message_type'] == MediusChatMessageType.WHISPER:
			dst_player = monolith.get_client_manager().get_player(serialized['target_id'])
			dst_player.send_mls(packet)
		else:
			raise Exception(f"Unimplemented chat message type: {serialized['chat_message_type']}")

		return []