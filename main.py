import os

from persist import read_file, update_file

# INITIAL VARIABLES
title = "focusly-cli"
helper = "Commands: add(a) | list(l) | done(d) | delete(del) | quit(q)"
width = 80
border = "═" * (width - 2)
filepath = "memory/list.json"
dir_path = "memory"


#CHECKING FILE ALREADY EXISTS
if os.path.isfile(filepath):
    tasks = read_file(filepath)
else:
    tasks = []


# FUNCTIONS
def add_task(task):
    if task != "..":
        tasks.append(task)
        print(f"{task} added to list")
        update_file(dir_path, filepath, tasks)


def list_tasks():
    if len(tasks) > 0:
        for i, value in enumerate(tasks):
            print(f"{i}. {value}")
    else:
        print("No items in list")


def done_task(task):
    # strikethrough ANSI sequence
    if task.isdigit():
        task = int(task)
        if 0 <= task <= len(tasks):
            tasks[task] = f"\033[9m{tasks[task]}\033[0m"
            list_tasks()
            update_file(dir_path, filepath, tasks)
    elif isinstance(task, str):
        idx = tasks.index(task)
        tasks[idx] = f"\033[9m{tasks[idx]}\033[0m"
        list_tasks()
        update_file(dir_path, filepath, tasks)
    else:
        print("Task not in list")


def delete_task(task):
    if task.isdigit():
        task = int(task)
        if 0 <= task <= len(tasks):
            tasks.pop(task)
            print(f"Deleted task {task}")
            list_tasks()
            update_file(dir_path, filepath, tasks)
    elif isinstance(task, str):
        if task in tasks:
            idx = tasks.index(task)
            tasks.pop(idx)
            print(f"Deleted task {task}")
            list_tasks()
            update_file(dir_path, filepath, tasks)
    else:
        print("Task not in list")


# MAIN
while True:
    # WELCOME/PROMPT
    print(
        f"""
    ╔{border}╗
    ║{title.upper().center(width - 2)}║
    ║{helper.center(width - 2)}║
    ╚{border}╝
    """
    )

    job = str(input("focusly ❯ "))

    # QUITTING
    if job == "quit" or job == "q" or job == "Q" or job == "exit":
        break

    # ADD TASK
    elif job == "add" or job == "a" or job == "A":
        while job != "..":
            job = str(input("focusly ❯ add ❯ ")).strip()
            add_task(job)

    # DISPLAY LIST
    elif job == "list" or job == "l" or job == "L":
        list_tasks()

    # MARK DONE
    elif job == "done" or job == "d" or job == "D":
        job = input("focusly ❯ done ❯ ")
        done_task(job)

    # DELETE TASK
    elif job == "delete" or job == "del" or job == "DEL" or job == "del":
        job = input("focusly ❯ delete ❯ ")
        delete_task(job)

    # ALT
    else:
        print("Invalid input")
