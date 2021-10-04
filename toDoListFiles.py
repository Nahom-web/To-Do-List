FILE = './Files/tasks.txt'


class FileNotFoundException(Exception):
    pass


class ToDoListFiles:

    def __init__(self):
        print(self._read_tasks())

    @staticmethod
    def _read_tasks():
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
