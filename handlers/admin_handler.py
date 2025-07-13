from aiogram import types, Dispatcher

async def admin_panel(message: types.Message):
    await message.answer("Admin paneliga xush kelibsiz!")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(admin_panel, commands=['admin'])
