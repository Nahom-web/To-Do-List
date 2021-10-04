# g40a01.py
# by Nahom Haile

import toDoList
import toDoListFiles


def start_program():
    print("Welcome")
    while True:
        try:
            task_input = input("")
            new_to_do_list = toDoList.ToDoList()
            if task_input != 0:
                stripped_task = task_input.split()
                command = stripped_task[0]
                if command == 'add':
                    print(new_to_do_list.add(stripped_task))
                elif command == 'upd':
                    new_to_do_list.update()
                elif command == 'rem':
                    new_to_do_list.remove()
                elif command == 'done':
                    new_to_do_list.completed_task()
                elif task_input == 'list all':
                    new_to_do_list.print_tasks(tasks_inp=new_to_do_list.list_all())
                elif command == 'purge':
                    new_to_do_list.list_incomplete()
                else:
                    raise ValueError()
        except ValueError:
            print("Please enter a valid command")


if __name__ == '__main__':
    toDoListFiles.ToDoListFiles._read_tasks()

    # start_program()
