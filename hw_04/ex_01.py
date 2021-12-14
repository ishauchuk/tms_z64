"""
The following iteration sequence is defined for a set of numbers:
If n is even n = n / 2. If n is odd n = n * 3 + 1.
Using the above rule and starting at 13, we generate a sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (from 13 to 1) contains 10 terms. Although this has not yet been proven (Collatz
problem), it is believed that all start numbers end in 1.
Which seed less than a million makes the longest chain?
NOTE: Once the chain starts, the terms can chain one million.
"""

from time import time


def collatz(n):
    start = time()
    target_num = 0
    longest = 0
    cache = {key: 0 for key in range(1, n)}

    for number in range(1, n):
        count = 1
        temp = number

        while temp > 1:
            if temp in cache and cache[temp] != 0:
                count += cache[temp]
                break
            if temp & 1 == 0:
                temp = temp // 2
            else:
                temp = 3 * temp + 1
            count += 1

        cache[number] = count
        if count > longest:
            longest = count
            target_num = number

    delta = (time() - start)
    print(f"The required number is {target_num} with sequence of "
          f"{longest} numbers was calculated in {delta:.5f} seconds.")


collatz(1000000)
