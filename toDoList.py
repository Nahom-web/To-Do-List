import task
import toDoListFiles


class NoPriorityNumberException(Exception):
    def __init__(self):
        self.message = "No priority number entered, please enter a number (1-4)"
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class PriorityNotANumberException(Exception):
    def __init__(self):
        self.message = "Priority number is not a number."
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class InvalidProjectNameException(Exception):
    def __init__(self):
        self.message = "No priority number entered, please enter a number (1-4)"
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class TooManyHashtagsInProjectNameException(Exception):
    def __init__(self):
        self.message = "Too many # in front of the project name."
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class InvalidProjectNameFormatException(Exception):
    def __init__(self):
        self.message = "Please enter a valid project name with a # in front."
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class InvalidPriorityNumberException(Exception):
    def __init__(self):
        self.message = "Please enter a number between 1 and 4"
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class ToDoList:
    TABLE_HEADERS = ['DESCRIPTION', 'COMPLETED', 'PRIORITY', 'PROJECT']

    def __init__(self):
        self.tasks = {}

    def increment_next_id(self):
        if len(self.get_all_tasks()) != 0:
            return int(list(self.get_all_tasks())[-1]) + 1
        else:
            return 1

    def add(self, task_input):
        if len(task_input) == 1 and task_input[0].lower() == "add":
            task_description_input = input("Enter task description>>>")
            task_completed_input = input("Enter Completed>>>")
            task_priority_input = input("Enter Priority>>>")
            task_project_input = input("Enter Project>>>")
        else:
            task_desc = ("".join(
                [name + " " for name in task_input if name != 'add' and '!' not in name and '#' not in name])).rstrip()

            task_priority = self.determine_priority(task_input)

            task_project = self.check_project_input(task_input)

        return 0

    def check_project_input(self, project):
        if project[0] != '#':
            raise InvalidProjectNameFormatException()
        if project.count('#') < 0 or project.count('#') > 1:
            raise TooManyHashtagsInProjectNameException()

    def determine_project(self, project):
        try:
            self.check_project_input(project)
            if len([p for p in project if '#' in p]) != 0:
                return ''.join([p for p in project if len(p[1:][0]) != 0])
            return None
        except InvalidProjectNameException:
            print(InvalidProjectNameException.__str__)
        except TooManyHashtagsInProjectNameException:
            print(TooManyHashtagsInProjectNameException.__str__)

    def check_priority(self, pr):
        if len(pr) == 0:
            raise NoPriorityNumberException()
        if not pr.isdigit():
            raise PriorityNotANumberException()
        if 1 > int(pr) > 4:
            raise InvalidPriorityNumberException()
        return True

    def determine_priority(self, priority):
        try:
            return [p for p in priority if '!' in p and self.check_priority(p[1:])][0]
        except NoPriorityNumberException:
            print(NoPriorityNumberException.__str__)
        except PriorityNotANumberException:
            print(PriorityNotANumberException.__str__)
        except InvalidPriorityNumberException:
            print(InvalidPriorityNumberException.__str__)

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
            print(
                '{0:<30} {1:>35} {2:>35} {3:>35}'.format({str(t.description)}, {str(t.project)}, {t.completed_string()},
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
