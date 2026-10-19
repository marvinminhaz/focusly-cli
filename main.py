# INITIAL VARIABLES
title = 'focusly-cli'
helper = 'Type add, list, done, delete, quit'
tasks = []


# FUNCTIONS
def add_task(task):
    if task != '..':
       tasks.append(task)
       print(f"{task} added to list")

def listTasks():
    if len(tasks) > 0:
        for i, value in enumerate(tasks):
            print(f'{i}. {value}')
    else:
        print("No items in list")

def doneTask(task):
    # strikethrough ANSI sequence
    if task.isdigit():
        task = int(task)
        if 0<=task<=len(tasks):
            tasks[task] = f"\033[9m{tasks[task]}\033[0m"
            listTasks()
    elif isinstance(task, str):
            idx = tasks.index(task)
            tasks[idx] = f"\033[9m{tasks[idx]}\033[0m"
            listTasks()
    else:
        print('Task not in list')

def deleteTask(task):
    if task.isdigit():
        task = int(task)
        if 0 <= task <= len(tasks):
            tasks.pop(task)
            print(f'Deleted task {task}')
            listTasks()
    elif isinstance(task, str):
        if task in tasks:
            idx = tasks.index(task)
            tasks.pop(idx)
            print(f'Deleted task {task}')
            listTasks()
    else:
        print('Task not in list')


# MAIN
while True:
    # LAUNCH
    print(f'''{title}
    {helper}''')

    job = str(input("focusly ❯ "))

    # QUITTING
    if job == 'quit' or job == 'q':
        break

    #ADD TASK
    elif job == 'add':
        while job != '..':
            job = str(input("focusly ❯ add ❯ "))
            add_task(job)

    #DISPLAY LIST
    elif job == 'list':
        listTasks()

    #MARK DONE
    elif job == 'done':
        job = input("focusly ❯ done ❯ ")
        doneTask(job)

    #DELETE TASK
    elif job == 'delete':
        job = input("focusly ❯ delete ❯ ")
        deleteTask(job)

    else:
        print("Invalid input")
