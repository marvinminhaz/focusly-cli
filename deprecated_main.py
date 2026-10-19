title = 'focusly-cli'
helper = 'Type add, list, done, delete, quit'

tasks = {}

#FUNCTIONS
def add_task(task):
    count = len(tasks)
    if task != '..':
       tasks[count + 1] = task
       print(f"{task} added to list")

def listTasks():
    if len(tasks) > 0:
        for k, v in tasks.items():
            print(f'{k}. {v}')
    else:
        print("No items in list")

def doneTask(taskNum):
    # strikethrough ANSI sequence
    if taskNum in tasks:
        tasks[taskNum] = f"\033[9m{tasks[taskNum]}\033[0m"
        listTasks()
    elif taskNum in tasks.values():
        for k, v in tasks.items():
            if v == taskNum:
                key = k
                tasks[key] = f"\033[9m{tasks[key]}\033[0m"
                listTasks()
    else:
        print('Task not in list')

def updateList():
    count = len(tasks)
    for v in tasks.values():
        tasks[count + 1] = v

def deleteTask(taskNum):
    total_items = len(tasks)
    tasks.pop(taskNum, 'Task not in list')
    for i in range(taskNum, total_items):
        tasks[i] = tasks[i+1]
    del tasks[total_items]
    total_items = total_items - 1
    listTasks()





while True:
    #WELCOME PROMPT
    print(f'''
            {title}
    {helper}
    ''')
    job = str(input("focusly ❯ "))
    #QUIT FOCUSLY
    if job == 'quit' or job == 'q':
        break
    #ADD TASKS
    elif job == 'add':
        while job != '..':
            job = str(input("focusly ❯ add ❯ "))
            add_task(job)
    #LIST TASKS
    elif job == 'list':
        listTasks()
    #MASK AS DONE
    elif job == 'done':
        job = input("focusly ❯ done ❯ ")
        if job.isdigit():
            doneTask(int(job))
        else:
            doneTask(job)
    #DELETE TASK
    elif job == 'delete':
        job = input("focusly ❯ delete ❯ ")
        if job.isdigit():
            deleteTask(int(job))
    #ALT
    else:
        print("Invalid input")
