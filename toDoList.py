import task


class ToDoList:

    tasks = {}
    tasks_commands = list()

    def __init__(self):
        self.tasks = {}

    def add_task_commands(self):
        commands = [
            'add',
            'rem',
            'done',
            'list',
            'purge'
        ]

        self.tasks_commands = commands

        return self.tasks_commands

    def tasks_initial_inserts(self):
        # Task Id
        # Description
        # Completed
        # Priority 1 - 4
        # Project

        self.tasks[0] = {
            'task_id': 1,
            'Description:': 'Study for Systems test',
            'Completed': False,
            'Priority': 1,
            'Project': 'School'
        }
        self.tasks[1] = {
            'task_id': 2,
            'Description:': 'Complete dev assignment',
            'Completed': False,
            'Priority': 2,
            'Project': 'School'
        }

        return self.tasks

    def add(self, task_list):
        new_task = task.Task()
        task_name = ""
        priority = 0
        project = ""
        for x in task_list:
            if x != 'add' and '!' not in x and '#' not in x:
                task_name += x + " "
            if '!' in x:
                if new_task.check_priority(x[1:]):
                    priority = x[1:]
                else:
                    # exception
                    print("Please enter a number between 1 and 4")
            if '#' in x:
                if new_task.check_project(x[1:]):
                    project = x[1:]
                else:
                    # exception
                    print("Please enter a valid project name")

        # if priority == 0:
        new_task.description = task_name
        new_task.completed = False
        if priority != 0:
            new_task.priority = priority
        if len(project) != 0:
            new_task.project = project
        print(new_task)
        return new_task

    def update(self):
        return self.tasks

    def remove(self):
        return self.tasks

    def completed_task(self):
        return self.tasks

    def list_all(self):
        return self.tasks

    def list_incomplete(self):
        return self.tasks

    def remove_completed_tasks(self):
        return self.tasks
