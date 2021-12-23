import threading
import os
import logging
from aiohttp import web
import asyncio
from time import sleep
import json
from logging import handlers
from datetime import datetime
import sqlite3

import os.path


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

        self._db_loc = db_loc
        self._db = db
        self._ip = ip
        self._port = port

        asyncio.run(self.main())

    def check_alts(self, username):
        c = self.conn.cursor()
        select = """SELECT hash
                    FROM alts WHERE username = ?;
                """
        vals = c.execute(select, [username]).fetchall()
        c.close()
        if not vals: # This already exists in the db
            return '[]'
        self._logger.info(vals)
        # Otherwise, we found some hashes. So let's find all usernames with this hash
        hashes = [f"'{val[0]}'" for val in vals]
        hashes = ', '.join(hashes)

        self._logger.info(f"Found hashes for username {username}: {hashes}")

        c = self.conn.cursor()
        select = f"""SELECT username
                    FROM alts WHERE hash in ({hashes});
                """
        self._logger.info(f"Executing: {select}")
        vals = c.execute(select).fetchall()
        self._logger.info(vals)
        c.close()

        vals = [val[0] for val in vals]
        return str(list(set(vals)))

    async def players(self, request):
        self._logger.debug("Players request!")
        name = request.match_info.get('name', "Anonymous")
        if name == 'Anonymous':
            return web.Response(text=f'You need a player name!')

        usernames = self.check_alts(name)

        return web.Response(text=usernames)

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

        db_file = os.path.join(self._db_loc, self._db)
        db_file = "file:" + db_file + "?mode=ro"

        while not os.path.isfile(os.path.join(self._db_loc, self._db)):
            self._logger.info(f"No backup db found! Waiting for creation ({os.path.join(self._db_loc, self._db)}) ...")
            sleep(10)

        self._logger.info("Connecting to backup db ...")
        self.conn = sqlite3.connect(db_file, uri=True)

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



