import os
import sys
import multiprocessing as mp
import time
import logging
from logging import handlers
import datetime

class RoboPacketSniffer:
	def __init__(self, config: dict):

		import subprocess
		import shlex
		cmd = "tcpdump --interface any -s 65535 -n -x 'udp port 51000 or tcp port 10075 or tcp port 10078 or tcp port 10079 or udp port 10070' -W 10 -C 1 -w /logs/pcap.pcap"
		args = shlex.split(cmd)
		p = subprocess.Popen(args)

		'''
		sys.path.append('pcap/pcap')
		try:
			from pcap.pcap.packet_sniffer import PacketSniffer
		except ImportError:
			g = input("Packet-Sniffer is not installed. Would you like to install that now? (y/n): ")
			while (g not in ['y','n']):
				g = input("(y/n): ")
			if g == 'y':
				os.system('cd pcap; git clone https://github.com/jtjanecek/Packet-Sniffer; mv Packet-Sniffer pcap')
				print("Module installed. Please restart robo.")
			else:
				print("Unable to run with packet sniffing.")
			sys.exit()

		mp.set_start_method('spawn')
		p = mp.Process(target=self.start, args=(config,), daemon=True)
		p.start()
		'''
		
	def start(self, config):
		self._logger = logging.getLogger("pcap")
		self._logger.info(config)
		self._logger.setLevel(logging.DEBUG)
		filehandler = handlers.RotatingFileHandler(os.path.join('logs','pcap.log'), mode='w', maxBytes=config['pcap']['log_maxbytes'], backupCount=config['pcap']['log_backup_count'])
		filehandler.setLevel(logging.DEBUG)
		self._logger.addHandler(filehandler)

		self._ports = {
			config['mas']['port'],
			config['mls']['port'],
			config['dmetcp']['port'],
			config['dmeudp']['port'],
			config['nat']['port'],
			config['api']['port']
		}

		try:
			from pcap.pcap.packet_sniffer import PacketSniffer
			packet_sniffer = PacketSniffer(config['pcap']['interface'])
			packet_sniffer.register(self)
			try:
				packet_sniffer.execute()
			except PermissionError:
				self._logger.error("Not enough permissions to run pcap. (Are you using sudo?)")
		except:
			self._logger.exception("Error in pcap")

	def update(self, packet):
		p = packet
		res = f'{datetime.datetime.now()} | '

		if 'IPv4' in p.protocol_queue:
			res += f'srcip: {p.ipv4.source:15} | dstip: {p.ipv4.dest:15} | '
			
			if 'TCP' in p.protocol_queue and 'PSH' in p.tcp.flag_txt and (p.tcp.sport in self._ports or p.tcp.dport in self._ports):
				res += f'TCP | srcprt: {p.tcp.sport:5} | dstport: {p.tcp.dport:5} | data: {self._bytes_to_hex(p.data)}'
				self._logger.debug(res)
			elif 'UDP' in p.protocol_queue and (p.udp.sport in self._ports or p.udp.dport in self._ports):
				res += f'UDP | srcprt: {p.udp.sport:5} | dstport: {p.udp.dport:5} | data: {self._bytes_to_hex(p.data)}'
				self._logger.debug(res)

	def _bytes_to_hex(self, data: bytes):
		return data.hex().upper()
