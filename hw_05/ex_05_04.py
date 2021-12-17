"""
Assignment: Calculating a Factorial
The factorial of a number is the product of all natural numbers up to and
including it. For example, the factorial of the number 5 is equal to
the product 1 * 2 * 3 * 4 * 5 = 120.
"""


def fact(n):
    facto = {key: 0 for key in range(n + 1)}
    facto[0], facto[1] = 1, 1

    for i in range(2, n + 1):
        facto[i] = facto[i - 1] * i
    print(facto[n])


n = int(input("Enter the number:\n"))
fact(n)
