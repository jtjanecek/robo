from utils.rtbufferdeframer import RtBufferDeframer
from utils import utils
import asyncio
from queue import Queue
from enums.enums import MediusPlayerStatus
import logging
logger = logging.getLogger("robo.player")

class Player():
    def __init__(self, account_id, username, session_key, mls_world_id, mls_con):
        # Basic info
        self._account_id = account_id
        self._username = username
        self._session_key = session_key
        self._mls_world_id = mls_world_id
        self._status = MediusPlayerStatus.MEDIUS_PLAYER_IN_CHAT_WORLD

        # Connection info
        self._mls_connection = mls_con
        self._dmetcp_connection = None
        self._dmeudp_connection = None

        # Buffers for packet fragmentation
        self._mls_deframe_buffer = RtBufferDeframer()
        self._dmetcp_deframe_buffer = RtBufferDeframer()
        self._dmeudp_deframe_buffer = RtBufferDeframer()

        # Game info
        self._game = None
        self._dmetcp_queue = Queue()
        self._dmeudp_queue = Queue()
        self._dmetcp_aggtime = 0.01
        self._dmeudp_aggtime = 0.01
        self._dmetcp_flush_task = None
        self._dmeudp_flush_task = None


    #############################################################
    # DME Sending data
    #############################################################

    def send_dmetcp(self, data: bytes):
        self._dmetcp_queue.put(data)

    def send_dmeudp(self, data: bytes):
        self._dmeudp_queue.put(data)

    def start_tcpflusher(self):
        self._dmetcp_flush_task = asyncio.create_task(self.tcpflusher())

    def start_udpflusher(self):
        self._dmeudp_flush_task = asyncio.create_task(self.udpflusher())

    async def tcpflusher(self):
        while True:
            size = self._dmetcp_queue.qsize()

            if size != 0:
                final_data = b''
                for i in range(size):
                    final_data += self._dmetcp_queue.get()
                self._dmetcp_connection.writer.write(final_data)
                await self._dmetcp_connection.writer.drain()
            await asyncio.sleep(self._dmetcp_aggtime)

    async def udpflusher(self):
        while True:
            size = self._dmeudp_queue.qsize()

            if size != 0:

                final_data = b''
                for _ in range(size):
                    popped = self._dmeudp_queue.get()
                    if len(final_data) + len(popped) > 500:
                        self._dmeudp_connection.send(final_data)
                        final_data = popped
                    else:
                        final_data += popped

                if final_data != b'':
                    self._dmeudp_connection.send(final_data)

            await asyncio.sleep(self._dmeudp_aggtime)

    def close(self):
        if self._dmetcp_flush_task != None:
            result = self._dmetcp_flush_task.cancel()
            if result == True:
                logger.info(f"Player [{self.__str__()}] successfully canceled TCP flush routine [{result}]")
            else:
                logger.error(f"Player [{self.__str__()}] was unable to cancel TCP flush routine [{result}]")
            self._dmetcp_flush_task = None

        if self._dmeudp_flush_task != None:
            result = self._dmeudp_flush_task.cancel()
            if result == True:
                logger.info(f"Player [{self.__str__()}] successfully canceled UDP flush routine [{result}]")
            else:
                logger.error(f"Player [{self.__str__()}] was unable to cancel UDP flush routine [{result}]")
            self._dmeudp_flush_task = None

    async def send_patch(self, packets: [bytes]):
        max_packet_size = 500
        packet_delay = .005

        for packet in packets:
            while len(packet) > max_packet_size:
                packet_mini = packet[0:max_packet_size]
                self.send_mls(packet_mini)
                packet = packet[max_packet_size:]
                await asyncio.sleep(packet_delay)
            self.send_mls(packet)
            await asyncio.sleep(packet_delay)


    #############################################################
    # MLS Sending data
    #############################################################

    def send_mls(self, data: bytes):
        logger.info(f"Sending MLS data to {self.__str__()}: {utils.bytes_to_hex(data)}")
        self._mls_connection.writer.write(data)
        asyncio.create_task(self.mlsflusher())

    async def mlsflusher(self):
        await self._mls_connection.writer.drain()

    def set_dmetcp_con(self, dmetcp_con):
        self._dmetcp_connection = dmetcp_con

    def set_dmeudp_con(self, dmeudp_con):
        self._dmeudp_connection = dmeudp_con

    def deframe(self, connection, data: [bytes]):
        '''
        We have to deframe within the connection, as packet fragmentation will occur and we need to save incomplete packets
        '''
        if connection.server_name == 'mls':
            return self._mls_deframe_buffer.deframe(data)
        elif connection.server_name == 'dmetcp':
            return self._dmetcp_deframe_buffer.deframe(data)
        elif connection.server_name == 'dmeudp':
            return self._dmeudp_deframe_buffer.deframe(data)

    def get_mls_world_id(self) -> int:
        return self._mls_world_id

    def set_mls_world_id(self, mls_world_id: int) -> None:
        self._mls_world_id = mls_world_id

    def get_account_id(self):
        return self._account_id

    def get_username(self):
        return self._username

    def get_dme_world_id(self) -> int:
        if self._game == None:
            return 0
        return self._game.get_dme_world_id()

    def get_player_status(self) -> MediusPlayerStatus:
        return self._status

    def set_player_status(self, status):
        self._status = status

    def set_game(self, game):
        self._game = game

    def get_game(self):
        return self._game

    def __str__(self):
        return f'Player(account_id={self._account_id},username={self._username},status={self._status},mls_world_id={self._mls_world_id},dme={self._game})'

    def get_dmetcp_ip(self):
        return self._dmetcp_connection.addr

    def set_dmetcp_aggtime(self, agg_time):
        self._dmetcp_aggtime = agg_time

    def set_dmeudp_aggtime(self, agg_time):
        self._dmeudp_aggtime = agg_time

    def get_dmetcp_aggtime(self):
        return self._dmetcp_aggtime

    def get_dmeudp_aggtime(self):
        return self._dmeudp_aggtime

    def to_json(self) -> dict:
        return {
            'status': self._status,
            'account_id': self._account_id,
            'username': self._username,
            'mls_world_id': self._mls_world_id,
            'dmetcp_aggtime': self._dmetcp_aggtime,
            'dmeudp_aggtime': self._dmeudp_aggtime
        }
