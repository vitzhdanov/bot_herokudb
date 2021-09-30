from aiogram import executor
from loader import dp
from utils.notify_admin import notify


async def on_startup(dp):
    await notify(dp)


if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp, on_startup=on_startup)