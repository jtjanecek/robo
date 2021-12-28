import threading
import os
import logging
from aiohttp import web
import asyncio
from time import sleep
import json
from logging import handlers
from datetime import datetime


from api.parser import weaponParser
from api.parser import advancedRulesParser
from api.parser import mapParser
from api.parser import timeParser
from api.parser import gamerulesParser


class Api():
    def __init__(self, monolith, ip: str, port: int, sync_rate: int, log_max_mb, log_backup_count, log_location):
        self._logger = logging.getLogger(f"robo.api")
        formatter = logging.Formatter('%(asctime)s API | %(levelname)s | %(message)s')
        filehandler = handlers.RotatingFileHandler(os.path.join(log_location,'api.log'), mode='w', maxBytes=log_max_mb*1000000, backupCount=log_backup_count)
        filehandler.setLevel(logging.DEBUG)
        filehandler.setFormatter(formatter)
        self._logger.addHandler(filehandler)

        self._players = "[]"
        self._games = "[]"
        self._chat = []

        self._monolith = monolith
        self._ip = ip
        self._port = port
        self._sync_rate = sync_rate

    async def monolith_sync(self):
        while True:
            self._logger.info("Syncing to monolith ...")

            # Sync player list
            players = self._monolith.api_req_players()
            self._players = json.dumps(players)

            # Sync game list
            games = self._monolith.api_req_games()
            for game in games:
                game['weapons'] = weaponParser(game['player_skill_level'])
                game['advanced_rules'] = advancedRulesParser(game['generic_field_3'])
                game['map'] = mapParser(game['generic_field_3'])
                game['game_length'] = timeParser(game['generic_field_3'])
                game_mode, submode = gamerulesParser(game['generic_field_3'])
                game['game_mode'] = game_mode
                game['submode'] = submode

                binary = bin(game['generic_field_3'])[2:]
                length = len(binary)
                leftover = 32 - length
                binary_full = leftover*'0' + binary
                if game_mode == 'CTF':
                    game['cap_limit'] = int(binary_full[5:9],2)
                elif game_mode == 'Deathmatch':
                    game['frag'] = int(binary_full[10:13],2)*5


            self._games = json.dumps(games)

            # Sync chat
            self._chat += self._monolith.api_req_chat()
            # only save last 10 minutes
            self._chat = [c for c in self._chat if (datetime.now().timestamp() - c['ts']) / 60 < 10]

            await asyncio.sleep(self._sync_rate)

    async def players(self, request):
        self._logger.debug("Players request!")
        return web.Response(text=self._players)

    async def games(self, request):
        self._logger.debug("Games request!")
        return web.Response(text=self._games)

    async def chat(self, request):
        self._logger.debug("Chat request!")
        self._logger.debug(self._chat)
        return web.Response(text=json.dumps(self._chat))

    async def start(self):
        # add stuff to the loop, e.g. using asyncio.create_task()

        app = web.Application()
        app.router.add_get('/players', self.players)
        app.router.add_get('/games', self.games)
        app.router.add_get('/chat', self.chat)

        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, self._ip, self._port)    
        await site.start()

        self._logger.info(f"Serving on ('{self._ip}', {self._port}) ...")


if __name__ == '__main__':
    a = Api()
    while True:
        sleep(100)
