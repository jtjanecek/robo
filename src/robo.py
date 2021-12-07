import os
from time import sleep
import json
import argparse

from pcap.robopacketsniffer import RoboPacketSniffer
from api.api import Api
from servers.tcpserver import TCPServer
from servers.udpserver import UDPServer
from infra.monolith import Monolith
import requests

import logging
import asyncio
from logging import handlers




class Robo():
    def __init__(self, config_file: str):
        config = self.read_config(config_file)

        logger = logging.getLogger('robo')
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s %(name)s | %(levelname)s | %(message)s')
        sh = logging.StreamHandler()
        sh.setFormatter(formatter)
        sh.setLevel(logging.getLevelName(config['console_log_level']))
        logger.addHandler(sh)
        filehandler = handlers.RotatingFileHandler(os.path.join(config['log_location'],'main.log'), mode='w', maxBytes=config['mls']['max_bytes_mb']*1000000, backupCount=5)
        filehandler.setFormatter(formatter)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(filehandler)

        self._monolith = Monolith(config)

        self._pcap = RoboPacketSniffer(config)    
        
        self._mas = TCPServer(self._monolith, 'mas', config['bind_ip'], config['mas']['port'], config['mas']['log_max_mb'], config['mas']['log_backup_count'], config['log_location'])
        self._mls = TCPServer(self._monolith, 'mls', config['bind_ip'], config['mls']['port'], config['mls']['log_max_mb'], config['mls']['log_backup_count'], config['log_location'])
        self._dmetcp = TCPServer(self._monolith, 'dmetcp', config['bind_ip'], config['dmetcp']['port'], config['dmetcp']['log_max_mb'], config['dmetcp']['log_backup_count'], config['log_location'])
        self._dmeudp = UDPServer(self._monolith, 'dmeudp', config['bind_ip'], config['dmeudp']['port'], config['dmeudp']['log_max_mb'], config['dmeudp']['log_backup_count'], config['log_location'])
        self._nat = UDPServer(self._monolith, 'nat', config['bind_ip'], config['nat']['port'], config['nat']['log_max_mb'], config['nat']['log_backup_count'], config['log_location'])
        self._api = Api(self._monolith, config['bind_ip'], config['api']['port'], config['api']['sync_rate'], config['api']['log_max_mb'], config['api']['log_backup_count'], config['log_location'])

        self.start()

    def read_config(self, config_file: str) -> dict:
        with open(config_file, 'r') as f:
            config = json.loads(f.read())

        if config['public_ip'] == '0.0.0.0':
            public_ip = requests.get('https://checkip.amazonaws.com').text.strip()
            config['public_ip'] = public_ip
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
    import argparse
    parser = argparse.ArgumentParser(description='Robo - Custom Medius server for UYA')
    parser.add_argument('--config', help='config file for this algo', required=True)
    cli_args = parser.parse_args()

    Robo(cli_args.config)
