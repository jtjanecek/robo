import os
from time import sleep
import json

from api.api import Api
from servers.tcpserver import TCPServer
from servers.udpserver import UDPServer
from infra.monolith import Monolith
import requests

import logging
import asyncio




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

		self._monolith = Monolith(config)
		
		self._mas = TCPServer(self._monolith, 'mas', config['mas']['ip'], config['mas']['port'])
		self._mls = TCPServer(self._monolith, 'mls', config['mls']['ip'], config['mls']['port'])
		self._dmetcp = TCPServer(self._monolith, 'dmetcp', config['dmetcp']['ip'], config['dmetcp']['port'])
		self._dmeudp = UDPServer(self._monolith, 'dmeudp', config['dmeudp']['ip'], config['dmeudp']['port'])
		self._nat = UDPServer(self._monolith, 'nat', config['nat']['ip'], config['nat']['port'])
		self._api = Api(self._monolith, config['api']['ip'], config['api']['port'], config['api']['sync_rate'])

		self.start()

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


	async def clear_zombie_games(self):
		while True:
			self._monolith.clear_zombie_games()
			await asyncio.sleep(120)

	async def misc_functions(self):
		# Add monolith sync to event loop
		asyncio.create_task(self.clear_zombie_games())
	
   	 	# wait forever
		await asyncio.Event().wait()

	def start(self):
		asyncio.run(self.misc_functions())

if __name__ == '__main__':
	Robo()
