from os import mkdir
from os.path import exists

def check():
    # startup functions
    check_database_dir()
    check_token_file()

def check_database_dir():
    if not exists("./data/database"):
        mkdir("./data/database")

def check_token_file():
    if not exists("./lib/bot/token"):
        open("./lib/bot/token", "w").close()
