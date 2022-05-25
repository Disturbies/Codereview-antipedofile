from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_menu = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton(text="Купить"),
			KeyboardButton(text="Баланс"),
			KeyboardButton(text="Информация")
		],
	],
	resize_keyboard=True
)


buy_button = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton(text="13-16 лет"),
			KeyboardButton(text="Износы"),
			KeyboardButton(text="Вписки")
		],
		[
			KeyboardButton(text="<< Назад")
		]
	],
	resize_keyboard=True
)


balance_button = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton(text="Пополнить баланс"),
			KeyboardButton(text="<< Назад")
		]
	],
	resize_keyboard=True
)


replenishment_methods_button = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton(text="Qiwi"),
			KeyboardButton(text="Карта")
		],
		[
			KeyboardButton(text="<< Назад")
		]
	],
	resize_keyboard=True
)


check_payments_button = ReplyKeyboardMarkup(keyboard=[
		[
			KeyboardButton(text="Проверить пополнение"),
			KeyboardButton(text="<< Назад")
		],
	],
	resize_keyboard=True
)