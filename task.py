
class Task:

    def __init__(self, _description, _completed, _priority, _project):
        self.description = _description
        self.completed = _completed
        self.priority = _priority
        self.project = _project

    def __str__(self):
        return f'Task added'


