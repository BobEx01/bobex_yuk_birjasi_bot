from aiogram import types
def register(dp):
    @dp.message_handler(commands=["start"])
    async def send_welcome(msg: types.Message):
        await msg.answer("Assalomu alaykum! BobEx botiga xush kelibsiz.")
