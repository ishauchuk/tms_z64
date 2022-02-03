"""
Write a decorator that can be called like this @decorator and this @decorator().
"""


def decorator(args=None):
    def some_decorator(func):
        def wrapper(*args, **kwargs):
            data = []
            data.extend(args)
            data = data[::-1]
            print(func.__name__)
            return func(*data)

        return wrapper

    if callable(args):
        return some_decorator(args)
    else:
        return some_decorator


if __name__ == "__main__":
    user_input = input('Enter data separated by spaces:\n').split(' ')


    @decorator
    def changeling_1(*args, **kwargs):
        print(*args, **kwargs)


    changeling_1(*user_input)


    @decorator()
    def changeling_2(*args, **kwargs):
        print(*args, **kwargs)


    changeling_2(*user_input)
