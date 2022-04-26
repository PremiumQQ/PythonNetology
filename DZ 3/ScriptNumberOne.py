import random

HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запращиваем у пользователя).
show - напечатать все добавленные задачи.
random - добавлять случайную задачу на дату Сегодня
"""
random_task =  ["Нечего не делать!!!", "Купить слона", "Съездить на карибы"]

tasks = {

}
run = True


def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date] = [task]
    print("Задача", task, " добавлена на дату:", date)


while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        date = input("Введите дату для отображения списка задач: ")
        if date in tasks:
            for task in tasks[date]:
                print('- ', task)
        else:
            print("Такой даты нет.")
    elif command == "add":
        task = input("Введите название задачи: ")
        date = input("Введите срок выполнения задачи: ")
        add_todo(date, task)
    elif command == "exit":
        break
    elif command == "random":
        task = random.choice(random_task)
        add_todo("Сегодня", task)
    else:
        print("Неизвестная команда")

print("Спасибо за использование! До свидания!")
