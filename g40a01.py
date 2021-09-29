# g40a01.py
# by Nahom Haile




def start_program():
    print("Welcome")
    task = input("")
    if task != 0:
        stripped_task = task.split()
        command = stripped_task[0]
        if command == 'add':
            add_to_tasks(stripped_task)
        elif command == 'upd':
            print()
        elif command == 'rem':
            print()
        elif command == 'done':
            print()
        elif command == 'list':
            print()
        elif command == 'purge':
            print()
        else:
            print()


if __name__ == '__main__':
    tasks_initial_inserts()
    start_program()