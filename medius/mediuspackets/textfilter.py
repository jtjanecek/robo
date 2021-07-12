from enums.enums import MediusEnum, CallbackStatus
from utils import utils
from medius.mediuspackets.textfilterresponse import TextFilterResponseSerializer

class TextFilterSerializer:
	data_dict = [
		{'name': 'mediusid', 'n_bytes': 2, 'cast': None},
		{'name': 'message_id', 'n_bytes': MediusEnum.MESSAGEID_MAXLEN, 'cast': None},
		{'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
		{'name': 'buf', 'n_bytes': 2, 'cast': None},
		{'name': 'text_filter_type', 'n_bytes': 4, 'cast': utils.bytes_to_str},
		{'name': 'text', 'n_bytes': MediusEnum.CHATMESSAGE_MAXLEN, 'cast': None}
	]

class TextFilterHandler:
	def process(self, serialized, monolith, con):
		return [TextFilterResponseSerializer.build(
			serialized['message_id'],
			serialized['text'],
			CallbackStatus.PASS
		)]