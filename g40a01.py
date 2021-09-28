# g40a01.py
# by Nahom Haile

# Constants:

FILE = './Files/tasks.txt'


class Task:

    def __init__(self, _id, _description, _completed, _priority, _project):
        self.id = _id
        self.description = _description
        self.completed = _completed
        self.priority = _priority
        self.project = _project

    def __str__(self):
        return f'Task {self.id} is to {self.description}.'

    def is_completed(self):
        if self.completed:
            return 'completed'
        else:
            return 'not completed'


def tasks_initial_inserts():
    # Task Id
    # Description
    # Completed
    # Priority 1 - 4
    # Project

    tasks[0] = {
        'task_id': 1,
        'Description:': 'Study for Systems test',
        'Completed': False,
        'Priority': 1,
        'Project': 'School'
    }
    tasks[1] = {
        'task_id': 2,
        'Description:': 'Complete dev assignment',
        'Completed': False,
        'Priority': 2,
        'Project': 'School'
    }


def read_tasks():
    with open(FILE, "r") as reader:
        if len(reader.readlines()) != 0:
            for line in reader.readlines():
                print(line, end="")
        else:
            print('file empty')


def check_priority(priority_inp):
    if len(priority_inp) != 0:
        if priority_inp.isdigit():
            if 1 <= priority_inp <= 4:
                return True
    return False


def check_project(project_inp):
    return len(project_inp) != 0


def add_to_tasks(task_list):
    task = ""
    priority = 0
    project = ""
    for x in task_list:
        if x != 'add' and '!' not in x and '#' not in x:
            task += x + " "
        if '!' in x:
            if check_priority(x[1:]):
                priority = x[1:]
            else:
                # exception
                print("Please enter a number between 1 and 4")
        if '#' in x:
            if check_project(x[1:]):
                project = x[1:]
            else:
                # exception
                print("Please enter a valid project name")

    # if priority == 0:

    task_obj = Task(_id=1, _description=task, _completed=False, _priority=priority, _project=project)
    print(task_obj)


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
    tasks = {}
    tasks_initial_inserts()
    start_program()

