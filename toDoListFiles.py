FILE = './Files/tasks.txt'


class ToDoListFiles:

    def __init__(self):
        pass

    @staticmethod
    def read_tasks():
        with open(FILE, "r") as reader:
            if len(reader.readlines()) != 0:
                for line in reader.readlines():
                    print(line, end="")
            else:
                raise FileNotFoundException("Cannot find file")

    @staticmethod
    def write_task():
        return 0

    @staticmethod
    def save_tasks():
        return 0
