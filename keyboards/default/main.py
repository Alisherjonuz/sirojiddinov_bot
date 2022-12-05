from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='🏫 Litsey direktori 🏫'),
            KeyboardButton(text='ℹ️ Litsey haqida ma`lumot ℹ️'),
        ],
        [
            KeyboardButton(text='📍 Joylashuv 📍'),
            KeyboardButton(text='📚 Foydali kitoblar 📚'),
        ],
        [
            KeyboardButton(text='📊 Bot statistikasi 📊'),
            KeyboardButton(text='🤖 Bot uchun taklif 🤖'),
        ],
    ],
    resize_keyboard=True
)

useful_books = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='🇬🇧 English 🇬🇧'),
            KeyboardButton(text='🇷🇺 Rus tili 🇷🇺'),
        ],
        [
            KeyboardButton(text='📜 Tarix 📜'),
            KeyboardButton(text='📝 Ona tili 📝'),
        ],
        [
            KeyboardButton(text='🤵 Tarbiya 🤵'),
            KeyboardButton(text='🇯🇵 Yapon tili 🇯🇵'),
        ],
    ],
    resize_keyboard=True
)