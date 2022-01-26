"""
Make a decorator that calculates the RAM consumption for a script.
"""
from memory_profiler import profile as check_RAM

log = open("09_03_log.txt", "w+")


@check_RAM(stream=log)
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a


if __name__ == '__main__':
    my_func()
