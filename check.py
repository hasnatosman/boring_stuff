import random


def checkingEven(number):
    if number % 2 == 0:
        return 'Is an even number'
    else:
        return 'Is an odd number'


r = random.randint(0, 9)
x = checkingEven(r)
print(r, x)
