import os

FILE = './Files/Tasks.txt'


class FileEmptyException(BaseException):
    pass


class ToDoListFiles:

    def __init__(self):
        if not os.path.isfile(FILE):
            open(FILE, "x")

    @staticmethod
    def read_tasks():
        tasks = list()
        if os.path.isfile(FILE):
            with open(FILE, "r") as reader:
                for line in reader.readlines():
                    tasks.append(line)
            return tasks

    @staticmethod
    def save_task(task_added, id_):
        f = open(FILE, "a")
        f.write(f'\r{id_}~{task_added["description"]}~{task_added["completed"]}~{task_added["priority"]}~'
                f'{task_added["project"]}')
        f.close()

    @staticmethod
    def write_all_tasks(list_of_tasks):
        fl = open(FILE, "w")
        for task_id, task in list_of_tasks.items():
            fl.write(f'{task_id}~{task["description"]}~{task["completed"]}~{task["priority"]}~{task["project"]}\n')
        fl.close()
