from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

button_calc = KeyboardButton(text='Рассчитать')
button_info = KeyboardButton(text='Информация')
kb_start = ReplyKeyboardMarkup(resize_keyboard=True)
kb_start.row(button_calc, button_info)

kb_calc = InlineKeyboardMarkup(resize_keyboard = True)
button_inline_calc = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
button_inline_formulas = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
kb_calc.row(button_inline_calc, button_inline_formulas)


