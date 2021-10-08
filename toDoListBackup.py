import task
import toDoListFiles


class ToDoList:
    TABLE_HEADERS = ['DESCRIPTION', 'COMPLETED', 'PRIORITY', 'PROJECT']

    def __init__(self):
        self.tasks = {}

    def increment_next_id(self):
        if len(self.get_all_tasks()) != 0:
            return int(list(self.get_all_tasks())[-1]) + 1
        else:
            return 1

    def add(self, task_list):
        new_task = task.Task()

        task_name = ""
        priority = None
        project = None
        completed = False

        if task_list == 'add':
            return 0
        else:
            task_name = new_task.get_task_name(task_list)
            new_task.description = task_name
            priority = new_task.get_priority_number([x for x in task_list if '!' in x])

            if priority is not None:
                new_task.priority = priority

            project = new_task.get_project_name([x for x in task_list if '#' in x])

            if project is not None:
                new_task.project = project

            id = ToDoList.increment_next_id(self)
            self.tasks[id] = new_task
            files = toDoListFiles.ToDoListFiles()
            files.save_task(self.tasks[id], id)
            return self.tasks[id]

    # def add_from_input(self, new_task_obj):
    #     task_name = input("Enter task description>>>")
    #     if new_task.check_task_name_input(task_name):
    #         new_task.description = task_name.rstrip()
    #     completed = input("Enter completed>>>")
    #     if new_task.check_completed_input(completed):
    #         new_task.description = task_name.rstrip()
    #     priority = input("Enter priority>>>")
    #     if new_task.check_priority(priority):
    #         new_task.description = task_name.rstrip()
    #     project = input("Enter project>>>")
    #     if new_task.check_project_input(project):
    #         new_task.description = task_name.rstrip()

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
        print('{0:<23} {1:>24} {2:>26} {3:>26}'.format(ToDoList.TABLE_HEADERS[0], ToDoList.TABLE_HEADERS[1],
                                                       ToDoList.TABLE_HEADERS[2], ToDoList.TABLE_HEADERS[3]))
        for id, t in tasks_inp.items():
            print('{0:<30} {1:>35} {2:>35} {3:>35}'.format({str(t.description)}, {str(t.project)}, {t.completed_string()},
                                                           {str(t.priority[1:])}))

    def get_all_tasks(self):
        file_tasks = toDoListFiles.ToDoListFiles.read_tasks()
        for task_ in file_tasks:
            stripped_task = task_.split('~')
            new_task = task.Task()
            new_task.description = stripped_task[1]
            new_task.completed = eval(stripped_task[2])
            new_task.priority = stripped_task[3]
            new_task.project = stripped_task[4].replace("\n", "")
            self.tasks[int(stripped_task[0])] = new_task
        return self.tasks
