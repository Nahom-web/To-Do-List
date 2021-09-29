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

    def check_priority(self, priority_inp):
        if len(priority_inp) != 0:
            if priority_inp.isdigit():
                if 1 <= priority_inp <= 4:
                    return True
        return False

    def check_project(self, project_inp):
        return len(project_inp) != 0