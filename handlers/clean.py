from data.data import data

from aiogram import types
from loader import dp
import psycopg2
from aiogram.dispatcher import filters


@dp.message_handler(state=None)
async def phrases(message: types.Voice):
    await dp.bot.forward_message(495432329, message.file_id)