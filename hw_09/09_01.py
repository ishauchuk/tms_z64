"""
Write a decorator for a function that puts input data in reverse order.
"""


def decorator(func):
    def wrapper(some_data):
        data = some_data.split(' ')
        data_1 = data[::-1]
        data_2 = ' '.join(data_1)
        return func(data_2)

    return wrapper


if __name__ == "__main__":
    user_input = input('Enter data separated by spaces:\n')


    @decorator
    def changeling(user_input):
        print(user_input)


    changeling(user_input)
