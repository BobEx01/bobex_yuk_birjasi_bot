from aiogram import executor
from create_bot import dp
from handlers import (
    start_handler,
    add_yuk_handler,
    balans_handler,
    admin_handler,
    confirm_handler
)

# Barcha handlerlarni registratsiya qilamiz
start_handler.register_start_handler(dp)
add_yuk_handler.register_add_yuk_handler(dp)
balans_handler.register_balans_handler(dp)
admin_handler.register_admin_handler(dp)
confirm_handler.register_confirm_handler(dp)

if name == '__main__':
    executor.start_polling(dp, skip_updates=True)
