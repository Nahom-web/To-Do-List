# g40a01.py
# by Nahom Haile

import toDoList
import toDoListFiles


def start_program():
    print("Welcome")
    print('''Commands you can enter:
    1. 'add' for adding tasks
    2. 'upd' for updating task
    3. 'rem' for removing a task
    4. 'done' to complete a task
    5. 'list all' to list all your tasks
    6. 'list todo' to list all incomplete tasks ordered by priority
    7. 'purge' to remove all completed tasks''')
    new_to_do_list = toDoList.ToDoList()
    while True:
        try:
            task_input = input("")

            if task_input != 0:
                stripped_task = task_input.split()
                command = stripped_task[0]
                if command == 'add':
                    task_added = new_to_do_list.add(stripped_task)
                    print(f'Task # added.')
                elif command == 'upd':
                    new_to_do_list.update()
                elif command == 'rem':
                    new_to_do_list.remove()
                elif command == 'done':
                    new_to_do_list.completed_task()
                elif task_input == 'list all':
                    new_to_do_list.print_tasks(new_to_do_list.get_all_tasks())
                elif task_input == 'list todo':
                    new_to_do_list.print_tasks(new_to_do_list.list_incomplete())
                elif command == 'purge':
                    new_to_do_list.list_incomplete()
                else:
                    raise ValueError()
        except ValueError:
            print("Please enter a valid command")


if __name__ == '__main__':
    start_program()
