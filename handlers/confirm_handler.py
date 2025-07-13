from aiogram import types, Dispatcher

async def confirm(message: types.Message):
    await message.answer("Tasdiq funksiyasi ishlamoqda...")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(confirm, commands=['confirm'])
