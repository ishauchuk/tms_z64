"""
The largest palindromic product
A palindromic number is read equally in both directions.
The largest palindrome made up of two two-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made up of two three-digit numbers.
"""

largest = 0
cache = set()
for i in range(900, 1000):
    cache.add(i)
    for j in range(900, 1000):
        if j not in cache:
            temp = i * j
            if temp > largest and (str(temp) == str(temp)[::-1]):
                largest = temp

print(largest)
