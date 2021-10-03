# import asyncio
#
# from aiogram import types
# from loader import dp
# import psycopg2
# from data.data import *
# from aiogram.dispatcher import filters
# from datetime import datetime
#
#
# def picture():
#
#     dp.bot.send_message(chat_id=495432329, text='Photo')
#
#
#
# schedule.every().friday.at("08:59").do(picture)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)