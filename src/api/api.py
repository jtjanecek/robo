import threading
import os
import logging
from aiohttp import web
import asyncio
from time import sleep
import json
from logging import handlers


class Api():
	def __init__(self, monolith, ip: str, port: int, sync_rate: int, log_maxbytes, log_backup_count, log_location):
		self._logger = logging.getLogger(f"robo.api")
		formatter = logging.Formatter('%(asctime)s API | %(levelname)s | %(message)s')
		filehandler = handlers.RotatingFileHandler(os.path.join(log_location,'api.log'), mode='w', maxBytes=log_maxbytes, backupCount=log_backup_count)
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
		self._thread = threading.Thread(target = self.start)
		self._thread.setDaemon(True)
		self._thread.start()

	async def monolith_sync(self):
		while True:
			self._logger.info("Syncing to monolith ...")

			# Sync player list
			players = self._monolith.api_req_players()
			self._players = json.dumps(players)

			# Sync game list
			games = self._monolith.api_req_games()
			self._games = json.dumps(games)

			# Sync chat
			self._chat += self._monolith.api_req_chat()

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

	async def main(self):
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

		# Add monolith sync to event loop
		asyncio.create_task(self.monolith_sync())
	
   	 	# wait forever
		await asyncio.Event().wait()

	def start(self):
		asyncio.run(self.main())

if __name__ == '__main__':
	a = Api()
	while True:
		sleep(100)
