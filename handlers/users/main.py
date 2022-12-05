from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.main import main_menu
from keyboards.default.main import useful_books
from loader import dp, bot


# Rus tili BQACAgIAAxkBAAICkmN864gYkzei3SWgyXASoBKHpfaVAAI_IQACRgroSyHfYLXV0bBsKwQ
# work book BQACAgIAAxkBAAICmWN867fafySKXbdGNH1v5v8d3jnOAAJDIQACRgroSwl0BTcWPWdFKwQ
# student's book BQACAgIAAxkBAAICm2N869Getmjyvaxj2PfleaimbvAzAAJNIQACRgroS_xyzexrWwr0KwQ
# ona tili BQACAgIAAxkBAAICnWN86-Ppf9v1EJnHVo9afV5_7u8YAAJQIQACRgroS7Ud9LuaIaBuKwQ
# yapon tili BQACAgIAAxkBAAICn2N86_z9u28YDpQDuv0K_BOvKnkOAAJXIQACRgroS6Dx6W1bsDLCKwQ
# Tarix BQACAgIAAxkBAAICoWN87BC3eZIZyP9o0AZXcanfpQaUAAJZIQACRgroS34aOyVYBI21KwQ
# Tarbiya BQACAgIAAxkBAAICo2N87SFzz0DGN8aUel9WzTz6gh_zAAJgIQACRgroS7JC13e5C4A6KwQ


# Location


@dp.message_handler(text="📍 Joylashuv 📍")
async def bot_start(message: types.Message):
    await bot.send_location(latitude=41.28539, longitude=69.195017, chat_id=message.from_user.id, reply_markup=main_menu)
    await message.answer(text="🏫 100097, Toshkent sh. Chilonzor t. 9-mavze, 33-uy. 🏫")

# About liceum


@dp.message_handler(text="ℹ️ Litsey haqida ma`lumot ℹ️")
async def get_file_id_p(message: types.Message):
    photo_id = "AgACAgIAAxkBAANSY252kvr9Yh1HRgVhBi5n6nOykF8AAqTEMRvdwXFLKnrjZypQUDMBAAMCAAN4AAMrBA"
    await message.answer_photo(
        photo_id, caption="🌍web-site: www.sirojiddinovral.uz 🌍\n🏫 Litsey asoschisi: Sa’di Hasanovich Sirojiddinov 🏫\n🗓 Tashkil topgan sana: 1998-yil 16-iyul 🗓\n📞 Telefon raqami: +998(71)278-86-49 📞"
    )

# Liceum's director


@dp.message_handler(text="🏫 Litsey direktori 🏫")
async def get_file_id_p(message: types.Message):
    photo_id = "AgACAgIAAxkBAAONY255C0blQJlPGhsKjfdCgTPqDJYAArnEMRvdwXFLBDAGPwoaemwBAAMCAAN4AAMrBA"
    await message.answer_photo(
        photo_id, caption="\n\n\nℹ️ F.I.Sh: Shergaziеv Baxrom Ungboyеvich\n👨‍💼 Lavozimi: S.H.Sirojiddinov akademik litseyi direktori "
    )

# Returner photo's id


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def get_file_id_p(message: types.Message):
    await message.reply(message.document.file_id)

# Useful books


@dp.message_handler(text="📚 Foydali kitoblar 📚")
async def bot_start(message: types.Message):
    photo_id = "AgACAgIAAxkBAAIBXmN4-x6IHLEZt2IEs7DHtkLTsZ_VAAJCwDEbILrISztKznSoF6eZAQADAgADeQADKwQ"
    await message.answer_photo(
        photo_id, caption="🔽 Pastdagi tugmalardan birini tanlang 🔽\n\n✅ O'zingizga kerakli kitobni tanlang ✅", reply_markup=useful_books
    )

# Russian book

@dp.message_handler(text="🇷🇺 Rus tili 🇷🇺")
async def bot_start(message: types.Message):
    photo_id = "BQACAgIAAxkBAAICkmN864gYkzei3SWgyXASoBKHpfaVAAI_IQACRgroSyHfYLXV0bBsKwQ"
    await message.answer_document(
        photo_id, caption="🇷🇺 Rus tili 🇷🇺 kitobi sizga muntazir.", reply_markup=main_menu
    )

# English book

@dp.message_handler(text="🇬🇧 English 🇬🇧")
async def bot_start(message: types.Message):
    photo_id = "BQACAgIAAxkBAAICmWN867fafySKXbdGNH1v5v8d3jnOAAJDIQACRgroSwl0BTcWPWdFKwQ"
    photo_id_1 = "BQACAgIAAxkBAAICm2N869Getmjyvaxj2PfleaimbvAzAAJNIQACRgroS_xyzexrWwr0KwQ"
    await message.answer_document(
        photo_id, caption="🇬🇧 workbook 🇬🇧 Solutions book "
    )
    await message.answer_document(
        photo_id_1, caption="🇬🇧 student's 🇬🇧 Solutions book ", reply_markup=main_menu
    )

# Mother toungue book

@dp.message_handler(text="📝 Ona tili 📝")
async def bot_start(message: types.Message):
    photo_id = "BQACAgIAAxkBAAICnWN86-Ppf9v1EJnHVo9afV5_7u8YAAJQIQACRgroS7Ud9LuaIaBuKwQ"
    await message.answer_document(
        photo_id, caption="📝 Ona tili 📝 kitobi sizga muntazir.", reply_markup=main_menu
    )

# History book

@dp.message_handler(text="📜 Tarix 📜")
async def bot_start(message: types.Message):
    photo_id = "BQACAgIAAxkBAAICoWN87BC3eZIZyP9o0AZXcanfpQaUAAJZIQACRgroS34aOyVYBI21KwQ"
    await message.answer_document(
        photo_id, caption="📜 Tarix 📜 kitobi sizga muntazir.", reply_markup=main_menu
    )

# Edication book

@dp.message_handler(text="🤵 Tarbiya 🤵")
async def bot_start(message: types.Message):
    photo_id = "BQACAgIAAxkBAAICo2N87SFzz0DGN8aUel9WzTz6gh_zAAJgIQACRgroS7JC13e5C4A6KwQ"
    await message.answer_document(
        photo_id, caption="🤵 Tarbiya 🤵 kitobi sizga muntazir.", reply_markup=main_menu
    )

# Japan language book

@dp.message_handler(text="🇯🇵 Yapon tili 🇯🇵")
async def bot_start(message: types.Message):
    photo_id = "BQACAgIAAxkBAAICn2N86_z9u28YDpQDuv0K_BOvKnkOAAJXIQACRgroS6Dx6W1bsDLCKwQ"
    await message.answer_document(
        photo_id, caption="🇯🇵 Yapon tili 🇯🇵 kitobi sizga muntazir.", reply_markup=main_menu
    )


# Time table

# write your code here

# Connect with creator of this bot


@dp.message_handler(text="🤖 Bot uchun taklif 🤖")
async def bot_start(message: types.Message):
    photo_id = "AgACAgIAAxkBAAIBlWN4_laGwgapioXFFC4zAXwk_J1aAAJfwDEbILrIS369wWZy6S-wAQADAgADeQADKwQ"
    await message.answer_photo(
        photo_id, caption="✅ Taklifingizni ✅ shu 👉 @sirojiddinov_litsey_chat 👈 guruhga yuboring va biz taklifingizni ko'rib chiqib bu botni rivojlantirishga harakat qilamiz. ✊✊✊"
    )

# Cancel to page before
# write your code to this free place
