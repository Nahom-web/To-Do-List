FILE = './Files/tasks.txt'


class ToDoList:
    tasks = {}

    def __init__(self):
        self.tasks = {}

    def tasks_initial_inserts(self):
        # Task Id
        # Description
        # Completed
        # Priority 1 - 4
        # Project

        ToDoList.tasks[0] = {
            'task_id': 1,
            'Description:': 'Study for Systems test',
            'Completed': False,
            'Priority': 1,
            'Project': 'School'
        }
        ToDoList.tasks[1] = {
            'task_id': 2,
            'Description:': 'Complete dev assignment',
            'Completed': False,
            'Priority': 2,
            'Project': 'School'
        }

    def add(self, task_list):
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

        task_obj = ToDoList.Task(_id=1, _description=task, _completed=False, _priority=priority, _project=project)
        print(task_obj)

    def read_tasks(self):
        with open(FILE, "r") as reader:
            if len(reader.readlines()) != 0:
                for line in reader.readlines():
                    print(line, end="")
            else:
                print('file empty')
