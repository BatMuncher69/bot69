from datetime import datetime
from discord import Intents
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord import Embed
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

		super().__init__(
			command_prefix=PREFIX,
			owner_ids=OWNER_IDS,
			intents=Intents.all(),
		)

	
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
			embed.set_thumbnail(url=self.guild.icon_url)
			embed.set_image(url=self.guild.icon_url)
			await channel.send(embed=embed)


		else:
			print("bot reconnected")

	async def on_message(self, message):
		pass


bot  =Bot()


