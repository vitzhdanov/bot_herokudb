from aiogram import Dispatcher

from data.data import ADMIN_ID


async def notify(dp: Dispatcher):
    await dp.bot.send_message(ADMIN_ID, 'The hellhound fell of the chain 😈')