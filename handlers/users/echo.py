from aiogram import types
from keyboards.default.main import main_menu

from loader import dp, bot


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    photo_id = "AgACAgIAAxkBAAIBaWN4-3jcP6kokAtnfCLuqTDRF4tUAAJFwDEbILrISxr_u4YNw_I5AQADAgADeAADKwQ"
    await message.answer_photo(
        photo_id, caption="🧐 Uzur bunday buyruq topilmadi 🧐\n\n🔽 Pastdagi tugmalardan birini tanlang 🔽",reply_markup=main_menu
    )