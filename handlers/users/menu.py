import random

from aiogram import types

from keyboards.default import *
from loader import dp


@dp.message_handler(state="*")
async def HandlerButtons(message: types.Message):
	type_requests = message.text
	
	if type_requests == "Купить":
		await message.answer('Ни в чем себе не отказывай пупсик', reply_markup=buy_button)

	if type_requests == "Баланс":
		await message.answer("Ваш баланс 0 руб", reply_markup=balance_button)

	if type_requests == "Информация":
		await message.answer("'В этом боте вы можете купить паки сливов школьниц\nКаждый пак включает в себя 30 фото и 10 видео\nКаждому человеку выдается уникальный архив'")	
	
	if type_requests == "Пополнить баланс":
		await message.answer("Выберите способ пополнения", reply_markup=replenishment_methods_button)

	if type_requests == "Qiwi":
		await message.answer(f"Кошелек qiwi для оплаты +79516446519'\nКомментарий: {random.randint(192880, 248019)}\nВремя на оплату 15 минут\nПосле перевода средств, нажмите ПРОВЕРИТЬ ПОПОЛНЕНИЕ", reply_markup=check_payments_button)

	if type_requests == "Карта":
		await message.answer('Заявка на пополнение успешно создана.\nДля пополнения перейдите по ссылке и укажите сумму пополнения\nhttps://my.qiwi.com/GALYNA-SFqRRWdGmU', reply_markup=check_payments_button)	

	if type_requests == "Проверить пополнение":
		await message.answer("Платеж не найден'")

	if type_requests == "13-16 лет" or type_requests == "Износы" or type_requests == "Вписки":
		if type_requests == "13-16 лет": 
			price_product = 100

		elif type_requests == "Износы": 
			price_product = 150

		elif type_requests == "Вписки": 
			price_product = 200

		await message.answer(f"Стоимость данного пака фотографий и видео {price_product} рублей.\n\nДля приобретения пополните баланс")