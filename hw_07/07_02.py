"""
'ATM':

Starting requirements.
There is an ATM
* Dictionary with cuts of the form:
    {face value: quantity,. ... ... }
* F-tion of issuance, that is, we call this function ATM.f-ia (amount) and to
us displays a dictionary with bills equal to this amount.
For instance:
Introduced 485
Output {100: 3, 50: 3, 20: 1, 10: 1, 5: 1}

Advanced requirements:

Develop an algorithm for calculating the remaining bills so that they
the optimal amount remained (approximately the same number of denominations)

Maximum requirements:

Integrate user accounts into our ATM.
Authorization.
The percentage withdrawn by the bank.

"""

user_info = {
    "ihar": {
        "card_id": "001",
        "password": "1234",
        "money": 100500,
    },
    "serg": {
        "card_id": "002",
        "password": "1488",
        "money": 8800,
    },
    "alex": {
        "card_id": "003",
        "password": "1488",
        "money": 5553,
    },
}

denomination = [100, 50, 20, 10, 5]
number_bills = [21, 20, 19, 18, 17]
banknotes = dict(zip(denomination, number_bills))

bank_commission = 1.01
bk = bank_commission


def counter_sum_banknotes():
    sum_banknotes = 0
    for k, v in banknotes.items():
        sum_b = k * v
        sum_banknotes += sum_b
    return sum_banknotes


def out(number):
    temp = banknotes.copy()
    if number > counter_sum_banknotes():
        print('Choose a lower amount.')
    else:
        cache = number
        for i in range(len(denomination)):
            if denomination[i] != 5 and cache > denomination[i]:
                sum = cache // denomination[i]
                if banknotes.get(denomination[i + 1]) * denomination[i + 1] / \
                        cache - (denomination[i] * sum - 1) < 1:
                    sum -= 1
                    if banknotes.get(denomination[i]) < sum:
                        sum = banknotes.get(denomination[i])
            else:
                sum = cache // denomination[i]
            temp[denomination[i]] = sum
            banknotes[denomination[i]] -= sum
            cache = cache - sum * denomination[i]
        print(temp)


while True:
    choice = input('''
Please make your choice:
    1) Exit - press button '1';
    2) Authorization - press button '2'.
\n''')
    if choice in '1':
        break
    if choice == '2':
        login = input("Enter your login:\n")
        if user_info.get(login):
            PIN = input('Enter your password:\n')
            if user_info[login]['password'] == PIN:
                print('\nYou are successfully logged in')
                while True:
                    choices = input('''
Please make your choice:
    1) Exit - press button '1';
    2) Withdraw cash - press button '2';
    3) Check balance - press button '3';
    4) Change password - press button '4'.
\n''')
                    if choices == '1':
                        break
                    elif choices == '2':
                        number = int(input(
                        'Enter the amount of money in multiples of five:\n'))
                        if number * bk > user_info[login]['money'] or \
                                number % 5 != 0:
                            print('\nIt is impossible to issue this amount '
                                  'of money')
                        else:
                            out(number)
                            user_info[login]['money'] -= number * bk
                            print(
                                f'You took off {number}. Bank commission for \
a transaction {round(((bk - 1) * number), 4)}')
                    elif choices == '3':
                        print(
                            f"Your current balance is \
{user_info[login]['money']} rubles.")
                    elif choices == '4':
                        new_password_1 = input('Enter new password:\n')
                        new_password_2 = input(
                            'Enter new password once again:\n')
                        if new_password_1 == new_password_2:
                            user_info[login]['password'] = new_password_1
                        else:
                            print('Passwords are different')
                    else:
                        print('\nEnter 1, 2, 3 or 4\n')
    else:
        print('\nEnter 1 or 2\n')
