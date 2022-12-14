from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='đĢ Litsey direktori đĢ'),
            KeyboardButton(text='âšī¸ Litsey haqida ma`lumot âšī¸'),
        ],
        [
            KeyboardButton(text='đ Joylashuv đ'),
            KeyboardButton(text='đ Foydali kitoblar đ'),
        ],
        [
            KeyboardButton(text='đ Bot statistikasi đ'),
            KeyboardButton(text='đ¤ Bot uchun taklif đ¤'),
        ],
    ],
    resize_keyboard=True
)

useful_books = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='đŦđ§ English đŦđ§'),
            KeyboardButton(text='đˇđē Rus tili đˇđē'),
        ],
        [
            KeyboardButton(text='đ Tarix đ'),
            KeyboardButton(text='đ Ona tili đ'),
        ],
        [
            KeyboardButton(text='đ¤ĩ Tarbiya đ¤ĩ'),
            KeyboardButton(text='đ¯đĩ Yapon tili đ¯đĩ'),
        ],
    ],
    resize_keyboard=True
)