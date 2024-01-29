import telebot

bot = telebot.TeleBot('6581119743:AAFid2q4Wq1E-KQpgmfHxTspEDJIh_cUjTE')

# Команда /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Я Happy Bot, рад приветствавать вам! Буду дублировать все Ваши сообщения.')

# Сообщение
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.send_message(message.chat.id, message.text)

# Запуск бота
bot.polling()