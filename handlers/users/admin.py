from aiogram import types
from keyboards.default.main import main_menu
from loader import dp, bot
from handlers.users.statistic import users


@dp.message_handler(text='π Bot statistikasi π')
async def bot_start(message: types.Message):
    await message.answer(f"π€ Bot statistikasi π€\n\nπ€ Bot foydalanuvchilari soni: {users()}taπ€\n\nπ§βπ» Bot yaratuvchisi: @AlisherNumonov π§βπ»",reply_markup=main_menu)
    