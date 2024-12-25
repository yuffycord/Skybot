from bot.bot import bot
from os.path import join, dirname
from dotenv import load_dotenv
import os

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

bot.run(os.environ.get("TOKEN"))