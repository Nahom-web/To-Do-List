# g40a01.py
# by Nahom Haile
import task
import toDoList
import sys
import exceptions


new_to_do_list = toDoList.ToDoList()


def add_from_terminal():
    task_separately = task.Task([], True)
    task_description_input = input("Enter task description>>>")
    task_separately.description = task_separately.validate_description(task_description_input.split())

    task_completed_input = input("Enter Completed>>>")
    if task_separately.check_invalid_characters_in_completed(task_completed_input.split()):
        task_separately.completed = task_separately.validate_completed_state(task_completed_input, False)

    task_priority_input = input("Enter Priority>>>")
    if task_separately.check_invalid_characters_in_priority(task_priority_input.split()):
        task_separately.priority = task_separately.validate_priority(task_priority_input.split(), True)

    task_project_input = input("Enter Project>>>")
    if task_separately.check_invalid_characters_in_project(task_project_input.split()):
        task_separately.project = task_separately.validate_project(task_project_input.split(), True)

    task_added = new_to_do_list.add(task_separately, True)
    print(task_added)


def update_from_terminal(stripped_task):
    new_to_do_list.find_task_with_id(stripped_task[1])

    update_task_separately = task.Task([], True)
    updated_description = input("Enter new description>>>")
    if update_task_separately.check_invalid_characters_in_description(updated_description.split()):
        update_task_separately.description = update_task_separately.validate_description(
            updated_description.split(), True)

    updated_completed = input("Enter completed state>>>")
    if update_task_separately.check_invalid_characters_in_completed(updated_completed.split()):
        update_task_separately.completed = update_task_separately.validate_completed_state(
            updated_completed.split(), True)

    updated_priority = input("Enter new priority>>>")
    if update_task_separately.check_invalid_characters_in_priority(updated_priority.split()):
        update_task_separately.priority = update_task_separately.validate_priority(updated_priority
                                                                                   .split(), True)

    updated_project = input("Enter new project>>>")
    if update_task_separately.check_invalid_characters_in_project(updated_project.split()):
        update_task_separately.project = update_task_separately.validate_project(updated_project
                                                                                 .split(), True)

    updated_task = new_to_do_list.update(update_task_separately, stripped_task[1])
    print(updated_task)


def exit_from_terminal():
    if len(sys.argv) > 1:
        exit(-1)


def start_program():
    if len(sys.argv) == 1:
        print("Welcome")
        print('''Commands you can enter:
        1. 'add' for adding tasks
        2. 'upd' for updating task
        3. 'rem' for removing a task
        4. 'done' to complete a task
        5. 'list all' to list all your tasks
        6. 'list todo' to list all incomplete tasks ordered by priority
        7. 'purge' to remove all completed tasks''')
    while True:
        try:
            task_input = ""

            if len(sys.argv) > 1:
                task_input = " ".join(sys.argv[1:])

            if len(sys.argv) == 1:
                print()
                task_input = input("Enter command>>>")

            if len(task_input) != 0:
                stripped_task = task_input.split()
                command = stripped_task[0].lower()
                if command == 'add':
                    if len(stripped_task) == 1:
                        add_from_terminal()
                        exit_from_terminal()
                    else:
                        task_added = new_to_do_list.add(stripped_task)
                        print(task_added)
                        exit_from_terminal()
                elif command == 'upd':
                    if len(stripped_task) > 2:
                        updated_task = new_to_do_list.update(stripped_task)
                        print(updated_task)
                        exit_from_terminal()
                    if len(stripped_task) == 2:
                        update_from_terminal(stripped_task)
                        exit_from_terminal()
                elif command == 'rem':
                    print(new_to_do_list.remove(stripped_task[1:]))
                    exit_from_terminal()
                elif command == 'done':
                    print(new_to_do_list.completed_task(stripped_task[1:]))
                    exit_from_terminal()
                elif task_input == 'list all':
                    new_to_do_list.print_tasks(new_to_do_list.get_all_tasks())
                    exit_from_terminal()
                elif task_input == 'list todo':
                    list_todo = new_to_do_list.list_incomplete()
                    new_to_do_list.print_tasks(list_todo)
                    exit_from_terminal()
                elif command == 'purge':
                    print(new_to_do_list.remove_completed_tasks())
                else:
                    raise ValueError()
        except ValueError:
            print("Please enter a valid command")

        except exceptions.PriorityNotANumberException as e:
            print(e)

        except exceptions.InvalidProjectNameException as e:
            print(e)

        except exceptions.TooManyHashtagsInProjectNameException as e:
            print(e)

        except exceptions.TooManyExclamationMarksInPriorityNameException as e:
            print(e)

        except exceptions.InvalidFormatForProjectNameException as e:
            print(e)

        except exceptions.InvalidFormatForPriorityNameException as e:
            print(e)

        except exceptions.InvalidPriorityNumberException as e:
            print(e)

        except exceptions.InvalidCompletedInputException as e:
            print(e)

        except exceptions.EmptyDescriptionException as e:
            print(e)

        except exceptions.NoTaskIdException as e:
            print(e)

        except exceptions.MoreThanOneTaskIdException as e:
            print(e)

        except exceptions.TooManyEntriesForUpdate as e:
            print(e)

        except exceptions.CannotFindTaskException as e:
            print(e)

        except exceptions.InvalidDescriptionException as e:
            print(e)

        except FileExistsError as e:
            print(e)

        except FileNotFoundError as e:
            print(e)

        except AttributeError as e:
            print(e)


if __name__ == '__main__':
    start_program()
