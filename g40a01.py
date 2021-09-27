# class PhoneBook:
#
#     def __init__(self, _description, _completed, _priority, _project):


FILE = './Files/tasks.txt'


def add_to_phone_book():
    with open(FILE, 'a') as f:
        print(phone_book, file=f)


def phone_book_initial_inserts():
    phone_book[0] = {
        'Description:': 'Study for Systems test',
        'Completed': False,
        'Priority': 1,
        'Project': 'School'
    }
    phone_book[1] = {
        'Description:': 'Complete dev assignment',
        'Completed': False,
        'Priority': 2,
        'Project': 'School'
    }


def read_phone_book():
    with open(FILE, "r") as reader:
        if len(reader.readlines()) != 0:
            for line in reader.readlines():
                print(line, end="")
        else:
            print('file empty')


if __name__ == '__main__':
    phone_book = {}
    phone_book_initial_inserts()
    add_to_phone_book()