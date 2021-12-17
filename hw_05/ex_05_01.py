"""
Write a function that will check if all open brackets are closed in the correct
order in a string of any length,among any characters. The method must accept
the string and return True if all brackets are closed in the correct order,
otherwise False. Here are some examples:

1. ([{}]) - True.
2. ab3(#$%[pop]cvfs){kek} - True.
3. (["{]} - False
4. lol(kek{4eburek])}[ - False
"""


def brackets(string: str = '') -> bool:
    cache = []
    sequence = True
    for i in string:
        if i in '{[(':
            cache.append(i)
        elif i in '}])':
            if not cache:
                sequence = False
                break
            bracket_open = cache.pop()
            if bracket_open == '(' and i == ')':
                continue
            if bracket_open == '[' and i == ']':
                continue
            if bracket_open == '{' and i == '}':
                continue
            sequence = False

    if sequence:
        return True
    else:
        return False


list_check = [
    '([{}])',
    'ab3(#$%[pop]cvfs){kek}',
    '(["{]}',
    'lol(kek{4eburek])}['
]

for elem in list_check:
    print(f'{elem} - {brackets(elem)}')