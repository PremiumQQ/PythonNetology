import telebot
import random

token = "5357054264:AAFTcgYAqTNLNByDEiE49luX9K6YrEP6kcU"
bot = telebot.TeleBot(token)

HELP = """
/help - Вывести список доступных команд.
/add - добавить задачу в список (название задачи запращиваем у пользователя).
/show - напечатать все добавленные задачи.
/random - добавлять случайную задачу на дату Сегодня
"""
random_task =  ["Нечего не делать!!!", "Купить слона", "Съездить на карибы"]
tasks = {}


def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date] = [task]



@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=['add'])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    add_todo(date, task)
    text = "Задача: " + task + " добавлена на дату: " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['random'])
def random_add(message):
    date = "сегодня"
    task = random.choice(random_task)
    add_todo(date, task)
    text = "Задача: " + task + " добавлена на дату: " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['show'])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ""
    print(date, tasks)
    if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text + "[] " + task + "\n"
    else:
        text = "Задач на эту дату нету"
    bot.send_message(message.chat.id, text)

bot.polling(none_stop=True, interval=0)