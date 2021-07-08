import os
from time import sleep
import json

from servers.tcpserver import TCPServer
from servers.udpserver import UDPServer
from infra.monolith import Monolith

import logging





class Robo():
	def __init__(self):
		config = self.read_config()

		logger = logging.getLogger('robo')
		logger.setLevel(logging.DEBUG)
		formatter = logging.Formatter('%(asctime)s %(name)s | %(levelname)s | %(message)s')
		sh = logging.StreamHandler()
		sh.setFormatter(formatter)
		sh.setLevel(logging.getLevelName(config['console_log_level']))
		logger.addHandler(sh)
		filehandler = logging.FileHandler(os.path.join('logs','main.log'), mode='w')
		filehandler.setFormatter(formatter)
		logger.setLevel(logging.DEBUG)
		logger.addHandler(filehandler)

		monolith = Monolith(config)
		
		self._mas = TCPServer(monolith, 'mas', config['mas']['ip'], config['mas']['port'])
		self._mls = TCPServer(monolith, 'mls', config['mls']['ip'], config['mls']['port'])
		self._dmetcp = TCPServer(monolith, 'dmetcp', config['dmetcp']['ip'], config['dmetcp']['port'])
		self._dmeudp = UDPServer(monolith, 'dmeudp', config['dmeudp']['ip'], config['dmeudp']['port'])
		self._nat = UDPServer(monolith, 'nat', config['nat']['ip'], config['nat']['port'])

		while True:
			sleep(100)

	def read_config(self) -> dict:
		with open('config.json', 'r') as f:
			config = json.loads(f.read())
		return config

if __name__ == '__main__':
	Robo()
