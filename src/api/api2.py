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


class Api2():
    def __init__(self, db_loc, db, ip: str, port: int, log_max_mb, log_backup_count, log_location):
        self._logger = logging.getLogger(f"robo.api2")
        formatter = logging.Formatter('%(asctime)s API2 | %(levelname)s | %(message)s')
        filehandler = handlers.RotatingFileHandler(os.path.join(log_location,'api2.log'), mode='w', maxBytes=log_max_mb*1000000, backupCount=log_backup_count)
        filehandler.setLevel(logging.DEBUG)
        filehandler.setFormatter(formatter)
        self._logger.addHandler(filehandler)

        self._ip = ip
        self._port = port

        asyncio.run(self.main())

    async def players(self, request):
        self._logger.debug("Players request!")
        name = request.match_info.get('name', "Anonymous")
        if name == 'Anonymous':
            return web.Response(text=f'You need a player name!')

        

        return web.Response(text=f'players {name}')

    async def clans(self, request):
        self._logger.debug("Clans request!")
        name = request.match_info.get('name', "Anonymous")
        if name == 'Anonymous':
            return web.Response(text=f'You need a clan name!')
        return web.Response(text=f'clans {name}')

    async def chat(self, request):
        self._logger.debug("Chat request!")
        self._logger.debug(self._chat)
        return web.Response(text=json.dumps(self._chat))

    async def main(self):
        # add stuff to the loop, e.g. using asyncio.create_task()

        app = web.Application()
        app.router.add_get('/players/{name}', self.players)
        app.router.add_get('/clans/{name}', self.clans)

        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, self._ip, self._port)    
        await site.start()

        self._logger.info(f"Serving on ('{self._ip}', {self._port}) ...")

        # wait forever
        await asyncio.Event().wait()



