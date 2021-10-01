class Task:

    current_task_id = 1

    def __init__(self):
        self.id = self.current_task_id
        self.increment_next_id()
        self.description = ""
        self.completed = False
        self.priority = None
        self.project = None

    def __str__(self):
        return f'Task {self.id} added'

    def increment_next_id(self):
        next_id = self.current_task_id + 1
        return next_id

    def is_completed(self):
        if self.completed:
            return 'completed'
        else:
            return 'not completed'

    def check_priority(self, pr):
        if len(pr) != 0:
            if pr.isdigit():
                if 1 <= int(pr) <= 4:
                    return True
        return False

    def check_project(self, proj):
        return len(proj) != 0

    def get_task_name(self, task_list_inp):
        task_name = "".join([name + " " for name in task_list_inp if name != 'add' and '!' not in name and '#' not in name])
        return task_name

    def get_priority_number(self, task_list_inp):
        try:
            # self.check_priority(p[1:])
            priority_num = int([p[1:] for p in task_list_inp if '!' in p and self.check_priority(p[1:])][0])
            return priority_num
        except ValueError:
            print("Please enter a number between 1 and 4")

    def get_project_name(self, task_list_inp):
        try:
            project = [p[1:] for p in task_list_inp if '#' in p and self.check_project(p[1:])][0]
            return project
        except ValueError:
            print("Please enter a valid project name")
