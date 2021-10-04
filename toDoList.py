import task


class ToDoList:

    tasks = {}

    def __init__(self):
        self.tasks = {}

    def add(self, task_list):
        new_task = task.Task()

        task_name = new_task.get_task_name(task_list)

        priority = new_task.get_priority_number([x for x in task_list if '!' in x])

        project = new_task.get_project_name([x for x in task_list if '#' in x])

        new_task.description = task_name

        if priority is not None:
            new_task.priority = priority

        if project is not None:
            new_task.project = project

        ToDoList.tasks[str(new_task.task_id)] = {
            'Task_id': new_task.task_id,
            'Description': new_task.description,
            'Completed': False,
            'Priority': priority,
            'Project': project
        }

        return new_task.__str__()

    def update(self):
        return self.tasks

    def remove(self):
        return self.tasks

    def completed_task(self):
        return self.tasks

    def list_all(self):
        return ToDoList.tasks

    def list_incomplete(self):
        return self.tasks

    def remove_completed_tasks(self):
        return self.tasks

    def print_tasks(self, tasks_inp):
        for id, t in ToDoList.tasks:
            print(f'Task {id} is to {t.Description}. It is {t.is_completed()}.')
