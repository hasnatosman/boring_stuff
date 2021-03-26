import random
def phone(number):
    if number == 19:
        return "It is a GP number"
    elif number == 18:
        return  "It is a Robi number"
    elif number == 16:
        return 'It is Airtel Number'
    elif number == 19:
        return "It is a BanglaLink Number"
    elif number == 15:
        return 'It a Taletalk number'
    else:
        return 'It probably Not a phone number'

r = random.randint(14, 20)
x = phone(r)
print(r, x)