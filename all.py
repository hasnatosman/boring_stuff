import random

def random_digits(n):
    num = range(0, 10)
    lst = random.sample(num, n)
    return str(lst).strip('[]')

print(random_digits(3))
