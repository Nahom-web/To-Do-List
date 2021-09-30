class Task:

    def __init__(self, _id, _description, _completed, _priority, _project):
        self.id = _id
        self.description = _description
        self.completed = _completed
        self.priority = _priority
        self.project = _project

    def __str__(self):
        return f'Task {self.id} is to {self.description}.'

    def is_completed(self):
        if self.completed:
            return 'completed'
        else:
            return 'not completed'

    def check_priority(self, pr):
        if len(pr) != 0:
            if pr.isdigit():
                if 1 <= pr <= 4:
                    return True
        return False

    def check_project(self, proj):
        return len(proj) != 0
