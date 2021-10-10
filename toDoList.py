import task
import toDoListFiles
import exceptions

files = toDoListFiles.ToDoListFiles()


class ToDoList:
    TABLE_HEADERS = ['DESCRIPTION', 'COMPLETED', 'PRIORITY', 'PROJECT']

    def __init__(self):
        self.list_of_tasks = {}
        # self.get_all_tasks()

    def increment_next_id(self):
        if len(self.get_all_tasks()) != 0:
            return int(list(self.get_all_tasks())[-1]) + 1
        else:
            return 1

    def add(self, task_input, already_validated=False):
        if already_validated:
            new_task = task_input
        else:
            new_task = task.Task(task_input, already_validated)
        task_id = ToDoList.increment_next_id(self)
        self.list_of_tasks[task_id] = {
            'description': new_task.description,
            'completed': new_task.completed,
            'priority': new_task.priority,
            'project': new_task.project
        }
        files.save_task(self.list_of_tasks[task_id], task_id)
        return f'Task {task_id} added'

    def find_task_with_id(self, task_id):
        found_task = {x: y for x, y in self.get_all_tasks().items() if x == int(task_id)}
        if len(found_task) == 0:
            raise exceptions.CannotFindTaskException()
        return found_task

    def update(self, update_task_input, task_id_to_update=0):

        find_id = task_id_to_update if type(update_task_input) == task.Task else [x for x in update_task_input][1]

        if len(find_id) == 0:
            raise exceptions.NoTaskIdException()
        if len(find_id) > 1:
            raise exceptions.MoreThanOneTaskIdException()

        find_task = self.find_task_with_id(find_id)

        task_id = int([x for x, y in find_task.items()][0])

        attributes_to_update = update_task_input

        if type(update_task_input) == list:
            attributes_to_update = task.Task(update_task_input[2:], update_task=True)
            check_completed = [c for c in update_task_input[2:] if c.lower() == "false" or c.lower() == "true"]
            if len(check_completed) == 0:
                attributes_to_update.completed = ''

        find_task[task_id][
            "description"] = attributes_to_update.description if attributes_to_update.description != '' else \
            find_task[task_id]["description"]
        find_task[task_id]["completed"] = attributes_to_update.completed if attributes_to_update.completed != '' else \
            find_task[task_id]["completed"]
        find_task[task_id]["priority"] = attributes_to_update.priority if attributes_to_update.priority is not None \
            else find_task[task_id]["priority"]
        find_task[task_id]["project"] = attributes_to_update.project if attributes_to_update.project is not None else \
            find_task[task_id]["project"]

        self.list_of_tasks[task_id] = find_task[task_id]

        files.write_all_tasks(self.list_of_tasks)

        return f'Updated Task {task_id}'

    @staticmethod
    def find_task_id(task_input):
        return [i for i in task_input if i.isnumeric()]

    def remove(self, task_input):
        task_id_list = self.find_task_id(task_input)
        if len(task_id_list) == 1:
            task_id = int(task_id_list[0])
            task_to_remove = self.find_task_with_id(task_id)
            if len(task_to_remove) == 0:
                raise exceptions.CannotFindTaskException()
            removed_task = self.list_of_tasks.pop(task_id)
            files.write_all_tasks(self.list_of_tasks)
            return f'Removed Task {task_id}'
        raise exceptions.NoTaskIdException()

    def completed_task(self, task_input):
        task_id_list = self.find_task_id(task_input)
        if len(task_id_list) == 1:
            task_id = int(task_id_list[0])
            task_to_complete = self.find_task_with_id(task_id)
            if len(task_to_complete) == 0:
                raise exceptions.CannotFindTaskException()
            task_to_complete[task_id]["completed"] = 'True'
            files.write_all_tasks(self.list_of_tasks)
            return f'Marked task {task_id} as done'
        raise exceptions.NoTaskIdException()

    @staticmethod
    def sort_list_by_priority(incomplete_tasks):
        return {k: v for k, v in sorted(incomplete_tasks.items(), key=lambda item: int(item[1]["priority"][1]))}

    def list_incomplete(self):
        all_incomplete_tasks = {x: y for x, y in self.get_all_tasks().items() if y["completed"].lower() == "false"}
        incomplete_tasks_with_priority = {x: y for x, y in all_incomplete_tasks.items() if y["priority"] != "None"}
        incomplete_tasks_with_no_priority = {x: y for x, y in all_incomplete_tasks.items() if y["priority"] == "None"}
        sorted_list = self.sort_list_by_priority(incomplete_tasks_with_priority)
        sorted_list.update(incomplete_tasks_with_no_priority)
        return sorted_list

    def remove_completed_tasks(self):
        tasks_to_remove = {i: v for i, v in self.list_of_tasks.items() if v["completed"].lower() == "true"}
        for t_id, val in tasks_to_remove.items():
            removed_task = self.list_of_tasks.pop(t_id)
        files.write_all_tasks(self.list_of_tasks)
        return f'All completed tasks removed'

    @staticmethod
    def print_tasks(tasks_inp):
        lines = "".join(['-' for x in range(30)])
        if len(tasks_inp) == 0:
            print(f'No tasks added')
        for t_id, t in tasks_inp.items():
            print()
            print(f'{lines}Task {t_id}{lines}')
            print(f'Description: {(t["description"])} \nCompleted: {"No" if t["completed"] == "False" else "Yes"} \n'
                  f'Priority: {"No priority number" if t["priority"] == "None" else t["priority"][1]} \nProject Name: '
                  f'{"No project" if t["project"] == "None" else t["project"][1:]}')
            print()

    def get_all_tasks(self):
        file_tasks = files.read_tasks()
        for task_ in file_tasks:
            stripped_task = task_.split('~')
            self.list_of_tasks[int(stripped_task[0])] = {
                'description': stripped_task[1],
                'completed': stripped_task[2],
                'priority': stripped_task[3],
                'project': stripped_task[4].replace("\n", "")
            }
        return self.list_of_tasks
