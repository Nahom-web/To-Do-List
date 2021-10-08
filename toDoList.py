import task
import toDoListFiles


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


class EmptyDescriptionException(Exception):
    def __init__(self):
        self.message = "Please enter a description for your task"
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class InvalidCompletedInputException(Exception):
    def __init__(self):
        self.message = "Please enter False or True for completed"
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class ToDoList:
    TABLE_HEADERS = ['DESCRIPTION', 'COMPLETED', 'PRIORITY', 'PROJECT']

    def __init__(self):
        self.list_of_tasks = {}

    def increment_next_id(self):
        if len(self.get_all_tasks()) != 0:
            return int(list(self.get_all_tasks())[-1]) + 1
        else:
            return 1

    def add_to_list(self, d, c, pri, proj):
        # 'true' if True else 'false'
        new_task = task.Task(_description=d, _completed=c, _priority=pri, _project=proj)
        task_id = ToDoList.increment_next_id(self)
        self.list_of_tasks[task_id] = {
            'description': new_task.description,
            'completed': new_task.completed,
            'priority': new_task.priority,
            'project': new_task.priority
        }
        files = toDoListFiles.ToDoListFiles()
        files.save_task(self.list_of_tasks[task_id], task_id)
        return new_task.added_message(task_id)

    def add(self, task_input, completed=None):
        if completed is not None:
            self.add_to_list(task_input[0], completed, task_input[1], task_input[2])
        else:
            task_desc = self.determine_description(task_input)
            task_priority = self.determine_priority(task_input)
            task_project = self.determine_project(task_input)
            self.add_to_list(task_desc, False, task_priority, task_project)

    def determine_description(self, task_input):
        description = [d for d in task_input if d != 'add' and '!' not in d and '#' not in d]
        if len(description) == 0:
            raise EmptyDescriptionException()
        else:
            updated_description = " ".join(description)
            return updated_description.strip()

    def determine_completed(self, completed):
        if completed == "":
            return False
        if completed.lower() == "true" or completed.lower() == "false":
            return bool(completed.title())
        return None

    def determine_project(self, project):
        project_location = [x for x in project if '#' in x]
        if len(project_location) != 0:
            if project_location[0][0] != '#':
                raise InvalidProjectNameFormatException()
            if project_location.count('#') < 0 or project_location.count('#') > 1:
                raise TooManyHashtagsInProjectNameException()
        else:
            return None
        return ''.join([p for p in project_location if len(p[1:][0]) != 0])

    @staticmethod
    def _check_priority(pr):
        if not pr.isdigit():
            raise PriorityNotANumberException()
        if 1 > int(pr) > 4:
            raise InvalidPriorityNumberException()
        return True

    def determine_priority(self, priority):
        priority_location = [x for x in priority if '!' in x]
        if len(priority_location) != 0:
            return [p for p in priority if '!' in p and self._check_priority(p[1:])][0]
        else:
            return None

    def update(self, update_task_input):
        find_task = {x: y for x, y in self.get_all_tasks() if x == int(update_task_input[1])}
        # if len(find_task) == 1:
        #     if len(update_task_input) == 2:
        #         if '!' not in update_task_input and ''
        return self.list_of_tasks

    def remove(self):
        return self.list_of_tasks

    def completed_task(self):
        return self.list_of_tasks

    def list_incomplete(self):
        return {x: y for x, y in self.get_all_tasks().items() if y["completed"] == "False"}

    def remove_completed_tasks(self):
        return self.list_of_tasks

    @staticmethod
    def _print_tasks(tasks_inp):
        lines = "".join(['-' for x in range(30)])
        for t_id, t in tasks_inp.items():
            print(f'{lines}Task {t_id}{lines}')
            print(f'Description: {(t["description"])} \nCompleted: {t["completed"]} \n'
                  f'Priority: {"No priority number" if t["priority"] == "None" else t["priority"][1]} \nProject Name: '
                  f'{"No project" if t["project"] == "None" else t["project"][1:]}')
            print()

    def get_all_tasks(self):
        file_tasks = toDoListFiles.ToDoListFiles.read_tasks()
        for task_ in file_tasks:
            stripped_task = task_.split('~')
            self.list_of_tasks[int(stripped_task[0])] = {
                'description': stripped_task[1],
                'completed': (stripped_task[2]),
                'priority': stripped_task[3],
                'project': stripped_task[4].replace("\n", "")
            }
        return self.list_of_tasks
