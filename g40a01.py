# g40a01.py
# by Nahom Haile

import toDoList


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
                    if len(stripped_task) == 1:
                        task_description_input = input("Enter task description>>>")
                        task_desc = new_to_do_list.determine_description(task_description_input.split())

                        task_completed_input = input("Enter Completed>>>")
                        task_completed = new_to_do_list.determine_completed(task_completed_input)

                        task_priority_input = input("Enter Priority>>>")
                        task_priority = new_to_do_list.determine_priority(task_priority_input.split())

                        task_project_input = input("Enter Project>>>")
                        task_project = new_to_do_list.determine_project(task_project_input.split())

                        task_added = new_to_do_list.add([task_desc, task_priority, task_project], task_completed)
                        print(task_added)
                    else:
                        task_added = new_to_do_list.add(stripped_task)
                        print(task_added)
                elif command == 'upd':
                    new_to_do_list.update(task_input)
                elif command == 'rem':
                    new_to_do_list.remove()
                elif command == 'done':
                    new_to_do_list.completed_task()
                elif task_input == 'list all':
                    new_to_do_list._print_tasks(new_to_do_list.get_all_tasks())
                elif task_input == 'list todo':
                    new_to_do_list._print_tasks(new_to_do_list.list_incomplete())
                elif command == 'purge':
                    new_to_do_list.list_incomplete()
                else:
                    raise ValueError()
        except ValueError:
            print("Please enter a valid command")


if __name__ == '__main__':
    start_program()
