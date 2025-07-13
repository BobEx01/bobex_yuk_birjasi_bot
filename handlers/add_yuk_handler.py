from aiogram import types, Dispatcher

async def add_yuk(message: types.Message):
    await message.answer("Yuk qo‘shish funksiyasi ishlamoqda...")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(add_yuk, commands=['add_yuk'])
