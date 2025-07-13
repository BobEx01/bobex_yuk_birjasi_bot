from aiogram import Bot, Dispatcher, executor
from dotenv import load_dotenv
import os
import logging

from handlers import start_handler, add_yuk_handler, balans_handler, admin_handler, confirm_handler

load_dotenv()
API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

start_handler.register_handlers(dp)
add_yuk_handler.register_handlers(dp)
balans_handler.register_handlers(dp)
admin_handler.register_handlers(dp)
confirm_handler.register_handlers(dp)

if name == '__main__':
    executor.start_polling(dp, skip_updates=True)
