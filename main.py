from aiogram import executor
from create_bot import dp
from handlers import start_handler, add_yuk_handler, balans_handler, admin_handler, confirm_handler

# Handlarni ro'yxatdan o'tkazamiz
start_handler.register_handlers(dp)
add_yuk_handler.register_handlers(dp)
balans_handler.register_handlers(dp)
admin_handler.register_handlers(dp)
confirm_handler.register_handlers(dp)

async def on_startup(dispatcher):
    print("Bot ishga tushdi!")

if name == "__main__":
    from aiogram import executor
    executor.start_polling(dp, on_startup=on_startup)
