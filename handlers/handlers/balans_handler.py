from aiogram import types, Dispatcher

async def balans(message: types.Message):
    await message.answer("Balansingiz: 0 so'm")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(balans, commands=['balans'])
