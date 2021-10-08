class NoPriorityNumberException(Exception):
    pass


class PriorityNotANumberException(Exception):
    pass


class InvalidPriorityNumberException(Exception):
    pass


class InvalidProjectNameException(Exception):
    pass


class Task:

    def __init__(self, _description, _completed, _priority, _project):
        self.description = _description
        self.completed = _completed
        self.priority = _priority
        self.project = _project

    def __str__(self):
        return f'Task added'

    def completed_string(self):
        if self.completed:
            return 'completed'
        else:
            return 'not completed'

    def check_task_name_input(self, task_name):
        return '!' not in task_name and '#' not in task_name

    def check_completed_input(self, completed):
        return len(completed.strip()) == 0 or (bool(completed.title()) == True or bool(completed.title()) == False)

    def check_priority(self, pr):
        if len(pr) == 0:
            raise NoPriorityNumberException("No priority number entered, please enter a number (1-4)")
        if not pr.isdigit():
            raise PriorityNotANumberException("Priority number is not a number.")
        if 1 > int(pr) > 4:
            raise InvalidPriorityNumberException("Please enter a number between 1 and 4")
        return True

    def check_project_input(self, project):
        if project[0] != '#':
            raise InvalidProjectNameException("Please enter a valid project name with a # in front.")
        if project.count('#') < 0 or project.count('#') > 1:
            raise InvalidProjectNameException("Too many # in front of the project name.")

    def get_task_name(self, task_list_inp):
        task_name = "".join([name + " " for name in task_list_inp if name != 'add' and '!' not in name and '#' not in name])
        return task_name.rstrip()

    def get_priority_number(self, task_list_inp):
        if len(task_list_inp) != 0:
            priority_num = [p for p in task_list_inp if self.check_priority(p[1:])][0]
            return priority_num
        return None

    def get_project_name(self, task_list_inp):
        if len(task_list_inp) != 0:
            project = [p for p in task_list_inp if len(p[1:][0]) != 0]
            return ''.join(project)
        return None
