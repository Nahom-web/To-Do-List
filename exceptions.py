class PriorityNotANumberException(BaseException):
    def __init__(self):
        self.message = "Priority number is not a number."
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class InvalidProjectNameException(BaseException):
    def __init__(self):
        self.message = "Project name should be one word only. Please re-try"
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class TooManyHashtagsInProjectNameException(BaseException):
    def __init__(self):
        self.message = "Too many #'s in front of the project name."
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class TooManyExclamationMarksInPriorityNameException(BaseException):
    def __init__(self):
        self.message = "Too many !'s in front of the project name."
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class InvalidFormatForProjectNameException(BaseException):
    def __init__(self):
        self.message = "Please enter a valid project name with a # in front followed by the project name with no spaces"
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class InvalidFormatForPriorityNameException(BaseException):
    def __init__(self):
        self.message = "Please enter a valid priority number with a ! in front."
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class InvalidPriorityNumberException(BaseException):
    def __init__(self):
        self.message = "Please enter a number between 1 and 4"
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class EmptyDescriptionException(BaseException):
    def __init__(self):
        self.message = "Please enter a real description for your task"
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class InvalidDescriptionException(BaseException):
    def __init__(self):
        self.message = "Cannot add characters for description. Please re enter description with letters only a-z A-Z"
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class InvalidCompletedInputException(BaseException):
    def __init__(self):
        self.message = "Please enter False or True for completed"
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class NoTaskIdException(BaseException):
    def __init__(self):
        self.message = "Please enter an Id after the command"
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class MoreThanOneTaskIdException(BaseException):
    def __init__(self):
        self.message = "Please enter just one Id after the command"
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class TooManyEntriesForUpdate(BaseException):
    def __init__(self):
        self.message = "Too many arguments was passed into the update function"
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class CannotFindTaskException(BaseException):
    def __init__(self):
        self.message = "Can't find task with the specified id"
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'
