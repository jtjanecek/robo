from utils import utils
from enums.enums import MediusEnum, RtIdEnum, MediusChatMessageType
from medius.mediuspackets.chatfwdmessage import ChatFwdMessageSerializer

import logging
logger = logging.getLogger('robo.chat')

class ChatCommands:
	def __init__(self):
		pass

	def process_chat(self, player, text):

		self._set_agg_time(player, text)


	def _set_agg_time(self, player, text):
		if "!tagg" in text or "!uagg" in text:
			try:
				text_split = text.split()
				agg_time = int(text_split[1])

				if text_split[0] == '!tagg':
					player.set_dmetcp_aggtime(agg_time * 0.001)
					resp_text = f'0TCP Agg set to {agg_time}ms. WARNING: Experimental mod'
				else:
					player.set_dmeudp_aggtime(agg_time * 0.001)
					resp_text = f'0UDP Agg set to {agg_time}ms. WARNING: Experimental mod'

				# Send the player a whisper
				packet = [{'name': 'Server app'}, {'rtid': RtIdEnum.SERVER_APP}]
				packet.append({'payload':ChatFwdMessageSerializer.build(utils.str_to_bytes("",MediusEnum.MESSAGEID_MAXLEN), 
					0, "SYSTEM", MediusChatMessageType.WHISPER, utils.str_to_bytes(resp_text, MediusEnum.CHATMESSAGE_MAXLEN))})
				packet = utils.rtpacket_to_bytes(packet)
				player.send_mls(packet)

			except:
				logger.exception('error')

