import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram import F
from aiogram.types import Message,CallbackQuery
from valyuta import inline_menu,back_to,rubl,uan,doller,euro

TOKEN = "6632943217:AAFFo8SRjTxfvSq2_fjY9N4z0ufnnc3et1E" #Token kiriting
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(text="Assalomu alaykum. \nValyuta boimizga xush kelibsiz", reply_markup= inline_menu)

@dp.callback_query(F.data=="doller")
async def doller_kursi(callback:CallbackQuery):
    await callback.message.edit_text(text="Dollar kursi:\n",reply_markup=doller)

@dp.callback_query(F.data=="euro")
async def yevro_kursi(callback:CallbackQuery):
    await callback.message.edit_text(text="Euro kursi:\n",reply_markup=euro)

@dp.callback_query(F.data=="uan")
async def uan_kursi(callback:CallbackQuery):
    await callback.message.edit_text(text="Uan kursi:\n",reply_markup=uan)

@dp.callback_query(F.data=="rubl")
async def rubl_kursi(callback:CallbackQuery):
    await callback.message.edit_text(text="Rubl kursi:\n",reply_markup=rubl)

@dp.callback_query(F.data=="back")
async def orqaga_qayt(callback:CallbackQuery):
    await callback.message.edit_text(text="Assalomu alaykum. \nValyuta boimizga xush kelibsiz",reply_markup=back_to)

async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
