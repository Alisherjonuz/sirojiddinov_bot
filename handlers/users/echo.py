from aiogram import types
from keyboards.default.main import main_menu

from loader import dp, bot


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    photo_id = "AgACAgIAAxkBAAIBaWN4-3jcP6kokAtnfCLuqTDRF4tUAAJFwDEbILrISxr_u4YNw_I5AQADAgADeAADKwQ"
    await message.answer_photo(
        photo_id, caption="š§ Uzur bunday buyruq topilmadi š§\n\nš½ Pastdagi tugmalardan birini tanlang š½",reply_markup=main_menu
    )