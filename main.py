import os
import msvcrt
import time
from prompt_toolkit import prompt

tasks = []

def init():
    load()

def main():
    os.system('cls')

    print('~ ~      Task Manager        ~ ~')

    print_tasks()

    sel_menu()

def sel_menu():
    print('a = Add a task \nq = Quit \nd = Delete \ne = edit')
    user = msvcrt.getwch()

    os.system('cls')

    if str(user) == 'a':
        add()
    elif str(user) == 'q':
        save()
        quit()
    elif str(user) == 'd':
        delete()
    elif str(user) == 'e':
        edit()
    else:
        print('Invalid :( \nTry again pls')
        input()
        main()


def add():
    user = input('You`re next task: ')
    if user == '':
        print('Empty?')
        add()
    else:
        tasks.append(user)
        main()

def print_tasks():
    i: int = 0
    if len(tasks) == 0:
        print('No tasks')
    else:
        print('You`re tasks are:')
    for task in tasks:
        i = i+1
        print(i, task)
    print()

def delete():
    if len(tasks) != 0:
        print_tasks()

        num = input('Wich number to remove: ')

        try:
            num = int(num)
            try:
                tasks.pop(num-1)
                main()
            except IndexError:
                print('Something is kinda off :( \ntry again')
                msvcrt.getwch()
                os.system('cls')
                delete()

        except ValueError:
            print('Something is kinda off :( \ntry again')
            msvcrt.getwch()
            os.system('cls')
            delete()
    else:
        print('Empty \nwhat you tryna do?')
        time.sleep(1)
        main()

def edit():
    print_tasks()
    num = input('Wich number to edit: ')
    try:
        num = int(num)
        try:
            selected = tasks[num-1]
            edited_word = prompt('edit: ', default=selected)
            tasks[num-1] =  edited_word
            main()
            pass
        except IndexError:
            print('Something is kinda off :( \ntry again')
            msvcrt.getwch()
            os.system('cls')
            edit()

    except ValueError:
        print('Something is kinda off :( \ntry again')
        msvcrt.getwch()
        os.system('cls')
        delete()

def save():
    with open('save', 'w') as file:
        for elements in tasks:
            if elements == '':
                pass
            else:
                file.write(elements + '\n')
def load():
    with open('save', 'r') as file:
        for line in file.read().splitlines():
            tasks.append(line)



init()
try:
    main()
except KeyboardInterrupt:
    save()
    quit()
