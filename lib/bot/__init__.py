from datetime import datetime
from glob import glob
from discord import Intents
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from discord import Embed, File
from discord.ext.commands import Bot as BotBase
from os.path import exists
from discord.ext.commands import CommandNotFound
from lib.bot.startup import check
from os import listdir
check()

from lib.db import db

PREFIX = "+"
OWNER_IDS = [803658998040756245]



class Bot(BotBase):
	def __init__(self):
		self.PREFIX = PREFIX
		self.ready = False
		self.guild = None
		self.scheduler  = AsyncIOScheduler()

		db.autosave(self.scheduler)
		super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS, intents=Intents.all(),)

	def setup(self):
		for cog in listdir("./lib/cogs"):
			if cog.endswith(".py"):
				self.load_extension("lib.cogs.{}".format(cog[:-3]))
				print("Successfully loaded {}".format(cog))

		print("setup complete")

	def run(self, version):
		self.VERSION = version

		print("runnning setup...")
		self.setup()

		with open("./lib/bot/token", "r", encoding="utf-8") as tf:
			self.TOKEN =tf.read()

		print("running bot...")
		super().run(self.TOKEN, reconnect=True)

	async def rules_reminder(self):
		await self.stdout.send("drink milk.")

	async def on_connect(self):
		print("bot connected")

	async def on_disconnect(self):
		print("bot disconncted")

	async def on_error(self, err, *args, **kwargs):
		if err =="on_command_error":
			await args[0].send("something went wrong.")

			await self.stdout.send("An error has occured.") 

	async def on_command_error(self, ctx, exc):
		if isinstance(exc, CommandNotFound):
			pass

		elif hasattr(exc,"original"):
			raise exc.original

	async def on_ready(self):
		if not self.ready:
			self.ready = True
			self.guild = self.get_guild(293802705867243520)
			self.stdout = self.get_channel(798158042767818762)
			self.scheduler.add_job(self.rules_reminder, CronTrigger(day_of_week=0, hour=12, minute=0, second=0))
			self.scheduler.start()
			
			
			await self.stdout.send("fuck you")

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


