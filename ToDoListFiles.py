# by Nahom Haile
# Advanced Topics in Computer Science I
# ToDoListFiles.py
# Contains the ToDoListFiles class. The class handles all the file work: read and writes the tasks.

import os

FILE = './Files/Tasks.txt'


class FileEmptyException(BaseException):
    pass


class ToDoListFiles:

    def __init__(self):
        # if the file is not there, then create it.
        if not os.path.isfile(FILE):
            f = open(FILE, "x")

    @staticmethod
    def read_tasks():
        tasks = list()
        if os.path.isfile(FILE):
            with open(FILE, "r") as reader:
                for line in reader.readlines():
                    tasks.append(line)
            return tasks

    @staticmethod
    def write_all_tasks(list_of_tasks):
        fl = open(FILE, "w")
        for task_id, task in list_of_tasks.items():
            fl.write(f'{task_id}~{task["description"]}~{task["completed"]}~{task["priority"]}~{task["project"]}\n')
        fl.close()
