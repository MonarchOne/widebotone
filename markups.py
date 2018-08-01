from telebot import types

markup_cat = types.ReplyKeyboardMarkup()
markup_cat.row("Категория №1", 'Категория №2', 'Категория №3')
markup_cat.row('Категория №4', 'Категория №5', 'Категория №6')
markup_cat.row('Назад')
