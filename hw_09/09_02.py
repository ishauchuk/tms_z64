"""
Write a decorator with a parameter for a function that will 
remove Oleg from the list.
"""


def banned(argument):
    def outer(func):
        def wrapper(*args, **kwargs):
            data = []
            data.extend(args)
            new_some_list = (i for i in data if i.lower() != argument.lower())
            result = func(*new_some_list)

        return wrapper

    return outer


if __name__ == "__main__":
    some_list = ['Ihar', 'Alex', 'Serg', 'Dasha', 'Oleg']


    @banned('Oleg')
    def printer(*args, **kwargs):
        print(*args, **kwargs)


    printer(*some_list)
