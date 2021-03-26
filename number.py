def phone(number):
    if number == '017':
        return "It is a GP number"
    elif number == '018':
        return  "it is a Robi number"
    elif number == "016":
        return 'It is Airtel Number'
    elif number == '019':
        return "It is a BanglaLink Number"
    elif number == '015':
        return 'It a Taletalk number'
    else:
        return 'It probably Not a phone number'


num = input('Input a number: ')
print(phone(num))