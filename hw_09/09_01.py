"""
Write a decorator for a function that puts input data in reverse order.
"""


def decorator(func):
    def wrapper(*args, **kwargs):
        data = []
        data.extend(args)
        data = data[::-1]
        return func(*data)

    return wrapper


if __name__ == "__main__":
    user_input = input('Enter data separated by spaces:\n').split(' ')


    @decorator
    def changeling(*args, **kwargs):
        print(*args, **kwargs)


    changeling(*user_input)
