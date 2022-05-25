from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default import start_menu

from loader import dp


@dp.message_handler(CommandStart())
@dp.message_handler(text="<< Назад")
async def bot_start(message: types.Message):
	await message.answer(f"Привет, {message.from_user.first_name}! Здесь ты можешь хорошо провести время!", reply_markup=start_menu)
