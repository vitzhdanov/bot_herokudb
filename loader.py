from aiogram import Dispatcher, Bot, types
from data.data import *

bot = Bot(BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


