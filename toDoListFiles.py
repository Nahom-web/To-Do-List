FILE = './Files/Tasks.txt'


class FileEmptyException(BaseException):
    pass


class ToDoListFiles:

    @staticmethod
    def read_tasks():
        tasks = list()
        with open(FILE, "r") as reader:
            for line in reader.readlines():
                tasks.append(line)
        return tasks

    @staticmethod
    def save_task(task_added, id):
        f = open(FILE, "a")
        f.write(f'\r{id}~{task_added["description"]}~{task_added["completed"]}~{task_added["priority"]}~{task_added["project"]}')
        f.close()
