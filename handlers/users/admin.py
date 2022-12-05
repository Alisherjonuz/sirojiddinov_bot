from aiogram import types
from keyboards.default.main import main_menu
from loader import dp, bot
from handlers.users.statistic import users


@dp.message_handler(text='📊 Bot statistikasi 📊')
async def bot_start(message: types.Message):
    await message.answer(f"🤖 Bot statistikasi 🤖\n\n👤 Bot foydalanuvchilari soni: {users()}ta👤\n\n🧑‍💻 Bot yaratuvchisi: @AlisherNumonov 🧑‍💻",reply_markup=main_menu)
    