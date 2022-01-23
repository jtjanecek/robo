import os
import json

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
        filehandler = handlers.RotatingFileHandler(os.path.join(config['log_location'],'main.log'), mode='w', maxBytes=config['mls']['log_max_mb']*1000000, backupCount=5)
        filehandler.setFormatter(formatter)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(filehandler)

        self._monolith = Monolith(config)

        self._pcap = RoboPacketSniffer(config)

        self._loop = asyncio.get_event_loop()
        self._mas = TCPServer(self._monolith, 'mas', config['mas']['port'], config['mas']['log_max_mb'], config['mas']['log_backup_count'], config['log_location'])
        self._mls = TCPServer(self._monolith, 'mls', config['mls']['port'], config['mls']['log_max_mb'], config['mls']['log_backup_count'], config['log_location'])
        self._dmetcp = TCPServer(self._monolith, 'dmetcp', config['dmetcp']['port'], config['dmetcp']['log_max_mb'], config['dmetcp']['log_backup_count'], config['log_location'])
        self._dmeudp = UDPServer(self._monolith, 'dmeudp', config['dmeudp']['port'], config['dmeudp']['log_max_mb'], config['dmeudp']['log_backup_count'], config['log_location'])
        self._nat = UDPServer(self._monolith, 'nat', config['nat']['port'], config['nat']['log_max_mb'], config['nat']['log_backup_count'], config['log_location'])
        self._api = Api(self._monolith, config['api']['port'], config['api']['sync_rate'], config['api']['log_max_mb'], config['api']['log_backup_count'], config['log_location'])

        # Start the servers
        self._loop.create_task(self._mas.start())
        self._loop.create_task(self._mls.start())
        self._loop.create_task(self._dmetcp.start())
        self._loop.create_task(self._dmeudp.start())
        self._loop.create_task(self._nat.start())

        # Start API
        self._loop.run_until_complete(self._api.start())

        # Misc functions
        self._loop.create_task(self.clear_zombie_games())
        self._loop.create_task(self.update_leaderboards())

        self._loop.run_forever()

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
            await asyncio.sleep(60 * 2) # 2 minutes

    async def update_leaderboards(self):
        while True:
            # TODO: check if no players are online before updating leaderboards
            self._monolith.update_leaderboards()
            await asyncio.sleep(60 * 60) # 1 hour


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Robo - Custom Medius server for UYA')
    parser.add_argument('--config', help='config file for this algo', required=True)
    cli_args = parser.parse_args()

    Robo(cli_args.config)
