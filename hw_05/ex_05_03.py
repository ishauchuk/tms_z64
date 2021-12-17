"""
Task: Raising numbers to a power up to a specified limit.
Print the degrees of natural numbers not exceeding a given number n.
The user sets the exponent and the number n.
"""

exp = int(input("Enter the degree of a natural number:\n"))
num = int(input("Enter the set limit:\n"))

reverse_number = int(pow(num, 1 / exp))
for i in range(1, reverse_number):
    print(i * i, end=' ')
