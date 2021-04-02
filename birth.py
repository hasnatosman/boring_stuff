birthday = {
    'name': 'HASNAT',
    'birthYear': 1995,
    'birthMonth': 'December',
    'birthDate': 3
}

while True:
    print('Whats your name ?')
    name = input('My name is: ')
    if name == '':
        break
    if birthday['name'] == name.upper():
        print('His name is ' + birthday['name'] + '\nHis birth Year is ' + str(birthday['birthYear'])
              + '\nHis birth date is ' + str(birthday['birthDate']))
        break
    else:
        print('Name does not matched')
        break
