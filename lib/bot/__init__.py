from datetime import datetime
from discord import Intents
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord import Embed, File
from discord.ext.commands import Bot as BotBase
from os.path import exists
from discord.ext.commands import CommandNotFound

from lib.db import db

PREFIX = "+"
OWNER_IDS = [803658998040756245]


class Bot(BotBase):
	def __init__(self):
		self.PREFIX = PREFIX
		self.ready = False
		self.guild = None
		self.scheduler  = AsyncIOScheduler()
		self.check_token_file()

		db.autosave(self.scheduler)
		super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS, intents=Intents.all(),)

	
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

	async def on_error(self, err, *args, **kwargs):
		if err =="on_command_error":
			await args[0].send("something went wrong.")

			channel = self.get_channel(798158042767818762)
			await channel.send("An error has occured.") 

	async def on_command_error(self, ctx, exc):
		if isinstance(exc, CommandNotFound):
			pass

		elif hasattr(exc,"original"):
			raise exc.original

	async def on_ready(self):
		if not self.ready:
			self.ready = True
			self.guild = self.get_guild(293802705867243520)
			self.scheduler.start()
			

			channel = self.get_channel(798158042767818762)
			await channel.send("fuck you")

			embed = Embed(title="fuck you", description="Why are you gae.", 
				colour=0xFF0000, timestamp=datetime.utcnow())
			fields = [("Name", "Value", True),
					("Another field", "This field", True),
					("A non-inline field", "This field will appear on its own row.", False)]
			for name, value, inline in fields:
				embed.add_field(name=name, value=value, inline=inline)
			embed.set_author(name="bot69", icon_url=self.guild.icon_url)
			embed.set_footer(text="This is a footer")
			await channel.send(embed=embed)

			await channel.send(file=File("./data/images/1.png"))
			
			print("bot ready")
		else:
			print("bot reconnected")

	async def on_message(self, message):
		pass


bot = Bot()


