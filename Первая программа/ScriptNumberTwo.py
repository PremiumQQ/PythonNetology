HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запращиваем у пользователя).
show - напечатать все добавленные задачи.
"""
today = []
tomorrow = []
other = []
run = True

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print("Задачи на сегодня: ", today)
        print("Задачи на завтра: ", tomorrow)
        print("Задачи в остальнео время: ", other)
    elif command == "add":
        task = input("Введите название задачи: ")
        time = input("Введите срок выполнения задачи: ")
        if time == "Сегодня":
            today.append(task)
        elif time == "Завтра":
            tomorrow.append(task)
        else:
            other.append(task)
        print("Задача добавлена.")
    elif command == "exit":
        break
    else:
        print("Неизвестная команда")


print("Спасибо за использование! До свидания!")