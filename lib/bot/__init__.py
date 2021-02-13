from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase
from os.path import exists

PREFIX = "+"
OWNER_IDS = [803658998040756245]


class Bot(BotBase):
	def __init__(self):
		self.PREFIX = PREFIX
		self.ready = False
		self.guild = None
		self.Scheduler  = AsyncIOScheduler()
		self.check_token_file()

		super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS)
	
	@staticmethod
	def check_token_file():
		if not exists("./lib/bot/token"):
			open("./lib/bot/token", "w").close()

	def run(self, version):
		self.VERSION = version

		with open("./lib/bot/token", "r", encoding="utf-8") as tf:
			self.TOKEN =tf.read()

		print("running bot...")
		super().run(self.TOKEN, reconnect=True)

	async def on_connect(self):
		print("bot connected")

	async def on_disconnect(self):
		print("bot disconncted")

	async def on_ready(self):
		if not self.ready:
			self.ready = True
			self.guild = self.get_guild(293802705867243520)
			print("bot ready")

		else:
			print("bot reconnected")

	async def on_message(self, message):
		pass


bot  =Bot()


