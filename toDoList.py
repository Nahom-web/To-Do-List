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

    def add(self, task_list):
        new_task = task.Task()

        task_name = new_task.get_task_name(task_list)

        priority = new_task.get_priority_number(task_list)

        project = new_task.get_project_name(task_list)

        new_task.description = task_name

        if priority != 0:
            new_task.priority = priority

        if len(project) != 0:
            new_task.project = project

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
