print('Whats your name ? ')

name = input().lower()

if name == 'mary':
    print('Hello Mary !')

    print('Whats the password ? ')
    password = int(input())
    if password == 12345:
        print('Access granted!')
    else:
        print('Wrong password!!')
        print('Try again!')
else:
    print('Who are you?')
