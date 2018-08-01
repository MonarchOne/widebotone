import telebot
from telebot import types
import config
import markups as m

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start', 'help'])
def any_msg(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('📗Курсы', '⭐️Схемы', '📰 Лента')
    markup.row('🔔Популярное', '💰Подписка', '👫Партнерство')
    bot.send_message(message.chat.id,
                     "😎 Всегда хотел научиться дизайну? Выбери раздел дизайн и начни изучать эту нишу. Хочешь быть виртуозным сммщиком? Никто не мешает научиться, более 700 курсов у тебя под носом. Хочешь зарабатывать деньги? Найди любую схему с  заработком в интернете. ",
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == "📗курсы":
        bot.send_message(chat_id, 'Выберите нужную категорию:', reply_markup=m.markup_cat)
        

@bot.message_handler(content_types=['text'])
def back_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == "Назад":
        bot.send_message(chat_id, 'Выберите нужную категорию:', reply_markup=m.markup_cat)

bot.polling(none_stop=True)
