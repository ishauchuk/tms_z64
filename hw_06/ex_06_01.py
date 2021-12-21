"""
This is my version of Russian roulette.
"""

import random
import time

bullet = {
    'bullet_0': '◍',
    'bullet_1': '◍',
    'bullet_2': '◍',
    'bullet_3': '◍',
    'bullet_4': '◍',
    'bullet_5': '◍',
}


def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())


def print_drum():
    print("         ▼")
    print(f"         {cache.get(list_cache[0])} ")
    print(f"    {cache.get(list_cache[5])}        {cache.get(list_cache[1])}")
    print("         ⊛")
    print(f"    {cache.get(list_cache[4])}        {cache.get(list_cache[2])}")
    print(f"         {cache.get(list_cache[3])} ")
    print('*' * 20)
    time.sleep(1.5)


cache = bullet.copy()
list_cache = list(cache)
dead = random.choice(range(6))
bullet['bullet_' + str(dead)] = 1
print_drum()

while True:
    steps = random.choice(range(-6, 7))
    shift(list_cache, steps)
    if bullet.get(list_cache[0]) == 1:
        cache[list_cache[0]] = '◉'
        print("Sorry, you're a little bit dead 💀")
        print_drum()
        break
    cache[list_cache[0]] = '◎'
    print_drum()
