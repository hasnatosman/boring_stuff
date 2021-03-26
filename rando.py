from random import randint

def randInp(number):
    range_start = 10 **( number - 1)
    range_end = (10 ** number) - 1
    if randint(range_start, range_end) == 13:
        return 'It is a gp-skitto number'
    if randint(range_start, range_end) == 15:
        return 'It is a Teletalk number'
    if randint(range_start, range_end) == 16:
        return 'It is a Airtel number'
    if randint(range_start, range_end) == 17:
        return 'It is a GP number'
    if randint(range_start, range_end) == 18:
        return 'It is a Robi number'
    if randint(range_start, range_end) == 19:
        return 'It is a BL number'
    else:
        return 'It is a normal number'


x = randInp(2)
print( x)