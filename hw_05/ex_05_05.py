"""
Task: Fibonacci numbers
Fibonacci numbers are a series of numbers in which each next number is equal
to the sum of the two previous ones: 1, 1, 2, 3, 5, 8, 13, .... Sometimes
the row starts from zero: 0, 1, 1, 2, 3, 5, .... In this case, we will stick
to the first option.
"""


def fib(n):
    fibo = {key: 0 for key in range(n + 1)}
    fibo[0], fibo[1] = 0, 1

    for i in range(2, n + 1):
        fibo[i] = fibo[i - 1] + fibo[i - 2]
    print(f'Fibonacci number for {n} is {fibo[n]}.')


n = int(input("Enter the number:\n"))
fib(n)
