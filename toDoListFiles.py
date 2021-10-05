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
    def save_task():
        return 0
