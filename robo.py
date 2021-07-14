import os
from time import sleep
import json

from api.api import Api
from servers.tcpserver import TCPServer
from servers.udpserver import UDPServer
from infra.monolith import Monolith
import requests

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
		self._api = Api(monolith, config['api']['ip'], config['api']['port'], config['api']['sync_rate'])

		while True:
			sleep(100)

	def read_config(self) -> dict:
		with open('config.json', 'r') as f:
			config = json.loads(f.read())

		if config['mls']['ip'] == '0.0.0.0':
			public_ip = requests.get('https://checkip.amazonaws.com').text.strip()
			config['mls']['public_ip'] = public_ip
			config['mas']['public_ip'] = public_ip
			config['nat']['public_ip'] = public_ip
			config['dmetcp']['public_ip'] = public_ip
			config['dmeudp']['public_ip'] = public_ip
		else:
			config['mls']['public_ip'] = config['mls']['ip']
			config['mas']['public_ip'] = config['mas']['ip']
			config['nat']['public_ip'] = config['nat']['ip']
			config['dmetcp']['public_ip'] = config['dmetcp']['ip']
			config['dmeudp']['public_ip'] = config['dmeudp']['ip']
		return config

if __name__ == '__main__':
	Robo()
