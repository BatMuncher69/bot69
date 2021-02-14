from lib.bot import bot
from os.path import exists
from os import mkdir

if not exists("./data/database"):
    mkdir("./data/database")

VERSION = "0.0.8"

bot.run(VERSION)