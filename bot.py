import telebot
from telebot import types
import config
import markups as m

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start', 'help', 'back'])
def any_msg(message):
    bot.send_message(message.chat.id,
                     "😎 Всегда хотел научиться дизайну? Выбери раздел дизайн и начни изучать эту нишу. Хочешь быть виртуозным сммщиком? Никто не мешает научиться, более 700 курсов у тебя под носом. Хочешь зарабатывать деньги? Найди любую схему с  заработком в интернете. ",
                     reply_markup=m.markup)


@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == "📗курсы":
        bot.send_message(chat_id, 'Выберите нужную категорию:', reply_markup=m.markup_cat)
    elif text == "назад":
        bot.send_message(chat_id, 'Выберите нужную категорию:', reply_markup=m.markup)
        

bot.polling(none_stop=True)
