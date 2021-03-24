import random


def divis(number):
    if number % 5 == 0 and number % 2 == 0:
        return 'It must be round one'
    elif number % 2 == 0:
        return 'It is an even number'
    elif number % 5 == 0:
        return 'It divisible by five'
    else:
        return 'It is must be odd one'


r = random.randint(1, 101)
x = divis(r)
print(r, '!!', x)
