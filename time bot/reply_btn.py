from aiogram import types


async def reply_btn_func():
    btn =  types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    btn.add(
        types.KeyboardButton('Tashkent'),
        types.KeyboardButton('Portugal'),
        types.KeyboardButton('Brazil'),
        types.KeyboardButton('Los Angeles'),
        types.KeyboardButton('Detroit'),
        types.KeyboardButton('Shanghai'),
        types.KeyboardButton('Tokyo'),
        types.KeyboardButton('Moscow'),
        types.KeyboardButton('London'),
        types.KeyboardButton('New York')
    )

    return btn