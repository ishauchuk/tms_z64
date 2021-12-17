"""
Write a function, a program that takes 1 argument - a number from 0 to 1000,
and returning True if it is simple, and False otherwise
"""


def number(n):
    if n in [0, 1]:
        return False
    else:
        a = [True] * n
        for k in range(2, n):
            if a[k]:
                for m in range(2 * k, n, k):
                    a[m] = False
        if n:
            return True
        else:
            return False


n = int(input("Enter a number:\n"))

print(number(n))
