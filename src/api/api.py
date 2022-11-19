import threading
import os
import logging
from aiohttp import web
import asyncio
from time import sleep
import json
from logging import handlers
from datetime import datetime

import websockets

from api.parser import weaponParser
from api.parser import advancedRulesParser
from api.parser import mapParser
from api.parser import timeParser
from api.parser import gamerulesParser
from api.parser import get_clean_clan_tag_from_stats
from api.parser import parse_clanstats_wide

import queue

class Api():
    def __init__(self, monolith, port: int, sync_rate: int, log_max_mb, log_backup_count, log_location, log_level, websocket_port, websocket_enabled):
        self._logger = logging.getLogger(f"robo.api")
        formatter = logging.Formatter('%(asctime)s API | %(levelname)s | %(message)s')
        filehandler = handlers.RotatingFileHandler(os.path.join(log_location,'api.log'), mode='w', maxBytes=log_max_mb*1000000, backupCount=log_backup_count)
        filehandler.setLevel(logging.getLevelName(log_level))
        filehandler.setFormatter(formatter)
        self._logger.addHandler(filehandler)

        self._monolith = monolith
        self._ip = '0.0.0.0'
        self._port = port
        self._sync_rate = sync_rate

        self._chat_messages = []

        self._dme_queue = queue.Queue()
        self._monolith._api = self

        self._websocket_port = int(websocket_port)
        self._websocket_enabled = websocket_enabled

        self._websocket_delay = 30

    async def players(self, request):
        self._logger.debug("Players request!")

        # Sync player list
        players = self._monolith.api_req_players()
        players = json.dumps(players)

        return web.Response(text=players)

    async def games(self, request):
        self._logger.debug("Games request!")

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
            binary_full = leftover * '0' + binary
            if game_mode == 'CTF':
                game['cap_limit'] = int(binary_full[5:9], 2)
            elif game_mode == 'Deathmatch':
                game['frag'] = int(binary_full[10:13], 2) * 5

        games = json.dumps(games)
        return web.Response(text=games)

    async def chat(self, request):
        self._logger.debug("Chat request!")

        # Sync chat
        self._chat_messages += self._monolith.api_req_chat()
        # only save last 10 minutes
        self._chat_messages = [c for c in self._chat_messages if (datetime.now().timestamp() - c['ts']) / 60 < 10]

        return web.Response(text=json.dumps(self._chat_messages))

    async def alts(self, request):
        self._logger.debug("Alts request!")
        name = request.match_info.get('name', "Anonymous")
        if name == 'Anonymous':
            return web.Response(text=f'You need a player name!')

        usernames = self._monolith.api_req_check_alts(name)
        return web.Response(text=json.dumps(usernames))

    async def account_id(self, request):
        self._logger.debug("Account id request!")
        account_id = request.match_info.get('account_id', "Anonymous")
        if account_id == 'Anonymous':
            return web.Response(text=f'You need an account id!')

        data = self._monolith.api_req_account_id(int(account_id))
        return web.Response(text=json.dumps(data))

    async def account_username(self, request):
        self._logger.debug("Account username request!")
        username = request.match_info.get('username', "Anonymous")
        if username == 'Anonymous':
            return web.Response(text=f'You need an account username!')

        data = self._monolith.api_req_username(username)
        return web.Response(text=json.dumps(data))

    async def clan_id(self, request):
        self._logger.debug("Clan id request!")
        clan_id = request.match_info.get('clan_id', "Anonymous")
        if clan_id == 'Anonymous':
            return web.Response(text=f'You need a clan_id!')

        data = self._monolith.api_req_clan_id(int(clan_id))
        if data != {}:
            data['clan_tag'] = get_clean_clan_tag_from_stats(data['clan_stats'])
            data = parse_clanstats_wide(data)
        return web.Response(text=json.dumps(data))

    async def clan_name(self, request):
        self._logger.debug("Clan name request!")
        clan_name = request.match_info.get('clan_name', "Anonymous")
        if clan_name == 'Anonymous':
            return web.Response(text=f'You need a clan_name!')

        data = self._monolith.api_req_clan_name(clan_name)
        if data != {}:
            data['clan_tag'] = get_clean_clan_tag_from_stats(data['clan_stats'])
            data = parse_clanstats_wide(data)
        return web.Response(text=json.dumps(data))


    async def start(self):
        # add stuff to the loop, e.g. using asyncio.create_task()

        app = web.Application()
        app.router.add_get('/robo/players', self.players)
        app.router.add_get('/robo/games', self.games)
        app.router.add_get('/robo/chat', self.chat)
        app.router.add_get('/robo/alts/{name}', self.alts)
        app.router.add_get('/robo/accounts/id/{account_id}', self.account_id)
        app.router.add_get('/robo/accounts/username/{username}', self.account_username)
        app.router.add_get('/robo/clans/id/{clan_id}', self.clan_id)
        app.router.add_get('/robo/clans/name/{clan_name}', self.clan_name)

        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, self._ip, self._port)
        await site.start()

        self._logger.info(f"Serving on ('{self._ip}', {self._port}) ...")

    async def start_websocket(self):
        if self._websocket_enabled == 'True':
            await websockets.serve(self.on_websocket_connection, '0.0.0.0', self._websocket_port)
            self._logger.info(f"Websocket serving on ('0.0.0.0', {self._websocket_port}) ...")
            self._connected = set()

    async def flush_api_data(self):
        if self._websocket_enabled == 'True':
            while True:
                # Broadcast a message to all connected clients.
                qsize = self._dme_queue.qsize()
                for _ in range(qsize):
                    data = self._dme_queue.get()

                    # 30 second delay to websocket
                    while data['ts'] + self._websocket_delay > datetime.now().timestamp():
                        await asyncio.sleep(.01)

                    data = json.dumps(data)

                    if len(self._connected) > 0:
                        for connection in self._connected:
                            try:
                                await connection.send(data)
                            except Exception:
                                connection.connected = False
                await asyncio.sleep(.001)

    # TODO: add co-routine to flush out packets if queue is
    async def on_websocket_connection(self, websocket, path):
        self._logger.info(f"Websocket connection: {websocket.remote_address}")
        # Register.
        self._connected.add(websocket)
        websocket.connected = True
        try:
            while websocket.connected:
                await asyncio.sleep(.001)
        # except Exception:
        #     self._logger.exception("message2")
        finally:
            self._logger.info("Websocket disconnected!")
            # Unregister.
            self._connected.remove(websocket)

if __name__ == '__main__':
    a = Api()
    while True:
        sleep(100)
