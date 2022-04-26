from email import message

import telebot

token = "5357054264:AAFTcgYAqTNLNByDEiE49luX9K6YrEP6kcU"
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Игорь":
        bot.send_message(message.from_user.id, "Ба! Знакомые все лица!")
    elif message.text == "Вова":
        bot.send_message(message.from_user.id, "Ба! Знакомые все лица!")


bot.polling(none_stop=True, interval=0)
