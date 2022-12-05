from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.main import main_menu
from loader import dp, bot
from handlers.users.statistic import check_id, id_add


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    id = message.from_user.id
    await message.answer(f"Botning 🏘 bosh sahifasiga 🏘 xush kelibsiz!",reply_markup=main_menu)
    if check_id(id)==0:
        id_add(id)
