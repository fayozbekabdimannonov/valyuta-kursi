from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

inline_menu = InlineKeyboardMarkup(
    inline_keyboard= [

    [InlineKeyboardButton(text="doller",callback_data="doller"),
    InlineKeyboardButton(text="euro",callback_data="euro"),],

    [InlineKeyboardButton(text="uan",callback_data="uan"),],

    [InlineKeyboardButton(text="rubl",callback_data="rubl")],

    ]
)

doller = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text="doller: 12500 so`m",callback_data="price_doll"),],
    [InlineKeyboardButton(text="ortga",callback_data="back"),],
    ]
)

euro = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text="euro: 13500 so`m",callback_data="price_euro"),],
    [InlineKeyboardButton(text="ortga",callback_data="back"),],
    ]
)

uan = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text="uan: 1700 so`m",callback_data="price_uan"),],
    [InlineKeyboardButton(text="ortga",callback_data="back"),],
    ]
)

rubl = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text="rubl: 100 so`m",callback_data="price_rubl"),],
    [InlineKeyboardButton(text="ortga",callback_data="back"),],

    ]
)

back_to = InlineKeyboardMarkup(
    inline_keyboard= [

    [InlineKeyboardButton(text="doller",callback_data="doller"),
    InlineKeyboardButton(text="euro",callback_data="euro"),],

    [InlineKeyboardButton(text="uan",callback_data="uan"),],

    [InlineKeyboardButton(text="rubl",callback_data="rubl")],

    ]

)