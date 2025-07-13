from aiogram import Bot, Dispatcher, types, executor
from handlers import start_handler, add_yuk_handler, confirm_handler, balance_handler
import os
from dotenv import load_dotenv

load_dotenv()
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)

start_handler.register(dp)
add_yuk_handler.register(dp)
confirm_handler.register(dp)
balance_handler.register(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
