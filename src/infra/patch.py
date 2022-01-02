import asyncio
from utils import utils
from enums.enums import MediusEnum, RtIdEnum, MediusChatMessageType
from medius.rtpackets.servermemorypoke import ServerMemoryPokeSerializer


import logging
logger = logging.getLogger('robo.patch')

class PatchManager:
    def __init__(self, config):
        # patch collection by app id
        self.Patches = {
            10684: Patch(10684, 
                "./bin/patch-ntsc.bin", 0x000D0000, 
                "./bin/unpatch-ntsc.bin", 0x000E0000,
                eval(config['patch']['hook_addr']), "j")
        }

    def process_login(self, player):
        patch = self.Patches.get(10684)
        if patch is not None:
            patch.send(player)

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

        packets_to_send = []

        try:
            # reset hook
            if self.Hook > 0 and self.HookType == "j":
                packet = ServerMemoryPokeSerializer.build(self.Hook, utils.hex_to_bytes("0800E003"))
                packet = utils.rtpacket_to_bytes(packet)
                packets_to_send.append(packet)

            # send unpatch first
            if self.UnhookPayloadPath != "":
                packets_to_send += self.sendFile(player, self.UnhookPayloadPath, self.UnhookAddress, True)


            # send patch last
            if self.PayloadPath != "":
                packets_to_send += self.sendFile(player, self.PayloadPath, self.Address, True)
            
            logger.debug('sent patch to {0}'.format(player))

        except:
            logger.exception('error')

        # pass all packets to player method
        asyncio.create_task(player.send_patch(packets_to_send))
    # 
    def sendFile(self, player, path, address, hook):
        packets_to_send = []

        # determine hook
        hookValue = int(address / 4)
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
        packets_to_send.append(packet)

        # send hook
        if hook and hookValue > 0 and self.Hook > 0:
            packet = ServerMemoryPokeSerializer.build(self.Hook, utils.int_to_bytes_little(4, hookValue))
            packet = utils.rtpacket_to_bytes(packet)
            packets_to_send.append(packet)
        return packets_to_send

    # send patch to client
    def apply(self, player):
        return self.send(player)


