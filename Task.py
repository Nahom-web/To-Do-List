# by Nahom Haile
# Advanced Topics in Computer Science I
# Task.py
# Contains the Task class, it takes in a list of parameters and has flags according to what the objects are for
# when created. Validates the 4 main attributes: description, completed, priority, and project.

import Exceptions


class Task:

    def __init__(self, _task_parameters, adding_separately=False, update_task=False):
        if adding_separately is False:
            self.description = self.validate_description(_task_parameters, update_task)
            self.completed = self.validate_completed_state(_task_parameters, update_task)
            self.priority = self.validate_priority(_task_parameters, update_task)
            self.project = self.validate_project(_task_parameters, update_task)
        else:
            self.description = ""
            self.completed = ""
            self.priority = ""
            self.project = ""

    @staticmethod
    def get_description(_task_parameters):
        return [d for d in _task_parameters if d != 'add' and '!' not in d and '#' not in d]

    def validate_description(self, _task_parameters, can_be_empty=False):
        description = self.get_description(_task_parameters)
        # if your updating the description it can be empty.
        if can_be_empty and len(description) == 0:
            return ''
        if len(description) == 0:
            raise Exceptions.EmptyDescriptionException()
        return " ".join(description)

    @staticmethod
    def check_invalid_characters_in_description(description_input):
        if len(description_input) != 0:
            invalid_characters = [c for c in description_input if '!' not in c and '#' not in c]
            if len(invalid_characters) != 0:
                raise Exceptions.InvalidDescriptionException()
            return True
        return True

    @staticmethod
    def get_completed_state(_task_parameters):
        return [c for c in _task_parameters if c.lower() == "false" or c.lower() == "true"]

    def validate_completed_state(self, _task_parameters, can_be_empty=False):
        completed = self.get_completed_state(_task_parameters)
        if can_be_empty and len(completed) == 0:
            return ''
        elif len(completed) == 0:
            return False
        elif len(completed) == 1:
            return eval(completed[0].title())
        else:
            raise Exceptions.InvalidCompletedInputException()

    @staticmethod
    def check_invalid_characters_in_completed(completed_input):
        if len(completed_input) != 0:
            invalid_characters = [c for c in completed_input if c.lower() != "false" and c.lower() != "true"]
            if len(invalid_characters) != 0:
                raise Exceptions.InvalidCompletedInputException()
            return True
        return True

    @staticmethod
    def get_priority_number(_task_parameters):
        return [x for x in _task_parameters if '!' in x]

    @staticmethod
    def check_priority(pr):
        if not pr.isdigit():
            raise Exceptions.PriorityNotANumberException()
        if 1 > int(pr) > 4:
            raise Exceptions.InvalidPriorityNumberException()
        return True

    def validate_priority(self, _task_parameters, can_be_empty=False):
        priority_location = self.get_priority_number(_task_parameters)
        if can_be_empty and len(priority_location) == 0:
            return None
        if len(priority_location) > 1:
            raise Exceptions.TooManyExclamationMarksInPriorityNameException()
        if len(priority_location) == 1:
            if priority_location[0][0] != '!':
                raise Exceptions.InvalidFormatForPriorityNameException()
            if priority_location[0].count('!') > 1:
                raise Exceptions.TooManyExclamationMarksInPriorityNameException()
            return [p for p in _task_parameters if '!' in p and self.check_priority(p[1:])][0]
        if len(priority_location) < 1:
            return None

    @staticmethod
    def check_invalid_characters_in_priority(priority_input):
        invalid_characters = [x for x in priority_input if '!' not in x]
        if len(invalid_characters) != 0:
            raise Exceptions.InvalidFormatForPriorityNameException()
        return True

    @staticmethod
    def get_project_number(_task_parameters):
        return [x for x in _task_parameters if '#' in x]

    def validate_project(self, _task_parameters, can_be_empty=False):
        project_location = self.get_project_number(_task_parameters)
        if can_be_empty and len(project_location) == 0:
            return None
        if len(project_location) > 1:
            raise Exceptions.TooManyHashtagsInProjectNameException()
        if len(project_location) == 1:
            if project_location[0][0] != '#':
                raise Exceptions.InvalidFormatForProjectNameException()
            if project_location[0].count('#') > 1:
                raise Exceptions.TooManyHashtagsInProjectNameException()
        if len(project_location) < 1:
            return None

        return ''.join([p for p in project_location if len(p[1:][0]) != 0])

    @staticmethod
    def check_invalid_characters_in_project(project_input):
        invalid_characters = [x for x in project_input if '#' not in x]
        if len(invalid_characters) != 0:
            raise Exceptions.InvalidFormatForProjectNameException()
        return True
