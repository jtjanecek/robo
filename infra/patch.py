from utils import utils
from enums.enums import MediusEnum, RtIdEnum, MediusChatMessageType
from medius.rtpackets.servermemorypoke import ServerMemoryPokeSerializer

import logging
logger = logging.getLogger('robo.patch')

class PatchManager:
	def __init__(self):
		pass

	def process_login(self, player):
		self._send_patch(player)


	def _send_patch(self, player, patch):
		try:
			# Send the player a whisper
			packet = ServerMemoryPokeSerializer.build(0x000D0000, utils.bytes_from_hex("12345678"))
			packet = utils.rtpacket_to_bytes(packet)
			player.send_mls(packet)
			logger.debug('sent patch to {0}'.format(player))

		except:
			logger.exception('error')


# 
class Patch:

    ApplicationId = -1
    PayloadPath = ""
    Address = 0x0
    UnhookPayloadPath = ""
    UnhookAddress = 0x0
    Hook = 0x0
    HookType = ""

    def __init__(self, appId, payloadPath, address, unhookPayloadPath, unhookAddress, hook, hookType):
        self.ApplicationId = appId
        self.PayloadPath = payloadPath
        self.Address = address
        self.UnhookPayloadPath = unhookPayloadPath
        self.UnhookAddress = unhookAddress
        self.Hook = hook
        self.HookType = hookType
    
    # 
    def send(self, player):
        try:
            # reset hook
            if self.Hook > 0 and self.HookType == "j":
                packet = ServerMemoryPokeSerializer.build(self.Hook, utils.bytes_from_hex("03E00008"))
                packet = utils.rtpacket_to_bytes(packet)
                player.send_mls(packet)

            # send unpatch first
            if self.UnhookPayloadPath != "":
                self.sendFile(player, self.UnhookPayloadPath, self.UnhookAddress, True)


            # send patch last
            if self.PayloadPath != "":
                self.sendFile(player, self.PayloadPath, self.Address, True)
			
            logger.debug('sent patch to {0}'.format(player))

        except:
            logger.exception('error')

    # 
    def sendFile(self, player, path, address, hook):

        # determine hook
        hookValue = address / 4
        if self.HookType == "j":
            hookValue |= 0x08000000
        elif self.HookType == "jal":
            hookValue |= 0x0C000000
        else:
            hookValue = 0

        # load payload file
        in_file = open(path, "rb")
        data = in_file.read()
        in_file.close()

        # generate messages 
        packet = ServerMemoryPokeSerializer.build(address, data)
        packet = utils.rtpacket_to_bytes(packet)
        player.send_mls(packet)

        # send hook
        if hook and hookValue > 0 and self.Hook > 0:
            packet = ServerMemoryPokeSerializer.build(self.Hook, utils.int_to_bytes_little(4, hookValue))
            packet = utils.rtpacket_to_bytes(packet)
            player.send_mls(packet)

    # send patch to client
    def apply(self, player):
        return self.send(player)


# patch collection by app id
Patches = {
    11184: Patch(11184, 
        "./bin/patch-ntsc.bin", 0x000D0000, 
        "./bin/unpatch-ntsc.bin", 0x000E0000,
        0, "j")
}
