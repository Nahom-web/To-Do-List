import task
import toDoListFiles


class ToDoList:

    def __init__(self):
        self.tasks = {}

    def increment_next_id(self):
        last_id = self.get_all_tasks(self).keys()
        return int(list(self.tasks)[-1]) + 1

    def add(self, task_list):
        new_task = task.Task()

        task_name = ""
        priority = None
        project = None
        completed = False

        if task_list == 'add':
            task_name = input("Enter task description>>>")
            if new_task.check_task_name_input(task_name):
                new_task.description = task_name.rstrip()
            completed = input("Enter completed>>>")
            if new_task.check_completed_input(completed):
                new_task.description = task_name.rstrip()
            priority = input("Enter priority>>>")
            if new_task.check_priority(priority):
                new_task.description = task_name.rstrip()
            project = input("Enter project>>>")
            if new_task.check_project_input(project):
                new_task.description = task_name.rstrip()

        else:
            task_name = new_task.get_task_name(task_list)
            new_task.description = task_name
            priority = new_task.get_priority_number([x for x in task_list if '!' in x])
            project = new_task.get_project_name([x for x in task_list if '#' in x])

            if priority is not None:
                new_task.priority = priority

            if project is not None:
                new_task.project = project

            id = ToDoList.increment_next_id(self)

            self.tasks[id] = {
                'Description': new_task.description,
                'Completed': False,
                'Priority': priority,
                'Project': project
            }

            print(f'Task {id} added.')

    def update(self):
        return self.tasks

    def remove(self):
        return self.tasks

    def completed_task(self):
        return self.tasks

    def list_incomplete(self):
        task_list = [{key: value} for key, value in self.get_all_tasks().items() if value["Completed"] is False]
        for item in task_list:
            print(item)

    def remove_completed_tasks(self):
        return self.tasks

    def print_tasks(self, tasks_inp):
        for id, t in tasks_inp.items():
            new_task = task.Task()
            new_task.description = t["Description"]
            new_task.completed = t["Completed"]
            new_task.priority = t["Priority"]
            new_task.project = t["Project"]
            print(f'Task {id}: {new_task.description}, for {new_task.project}. Completed: {new_task.completed_string()}. '
                  f'{new_task.priority[1:]} in your list of priorities.')

    def get_next_task_number(self):
        return 0

    def get_all_tasks(self):
        file_tasks = toDoListFiles.ToDoListFiles.read_tasks()
        for task_ in file_tasks:
            stripped_task = task_.split('~')
            self.tasks[int(stripped_task[0])] = {
                'Description': stripped_task[1],
                'Completed': eval(stripped_task[2]),
                'Priority': stripped_task[3],
                'Project': stripped_task[4].replace("\n", "")
            }
        return self.tasks
