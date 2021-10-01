class NoPriorityNumberException(Exception):
    pass


class PriorityNotANumberException(Exception):
    pass


class InvalidPriorityNumberException(Exception):
    pass


class Task:

    next_task_id = 1

    def __init__(self):
        self.task_id = Task.next_task_id
        self.increment_next_id()
        self.description = ""
        self.completed = False
        self.priority = None
        self.project = None

    def __str__(self):
        return f'Task {self.task_id} added'

    def increment_next_id(self):
        Task.next_task_id += 1

    def is_completed(self):
        if self.completed:
            return 'completed'
        else:
            return 'not completed'

    def check_priority(self, pr):
        if len(pr) == 0:
            raise NoPriorityNumberException("No priority number entered, please enter a number (1-4)")
        if not pr.isdigit():
            raise PriorityNotANumberException("Priority number is not a number.")
        if 1 > int(pr) > 4:
            raise InvalidPriorityNumberException("Please enter a number between 1 and 4")
        return True

    def get_task_name(self, task_list_inp):
        task_name = "".join([name + " " for name in task_list_inp if name != 'add' and '!' not in name and '#' not in name])
        return task_name

    def get_priority_number(self, task_list_inp):
        if len(task_list_inp) != 0:
            priority_num = [p[1:] for p in task_list_inp if self.check_priority(p[1:])][0]
            return int(priority_num)
        return None

    def get_project_name(self, task_list_inp):
        if len(task_list_inp) != 0:
            project = [p[1:] for p in task_list_inp if len(p[1:][0]) != 0]
            return str(project)
        return None
