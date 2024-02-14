import telebot

bot = telebot.TeleBot('TG_TOKEN')

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()
