passwordFile = open('SecretPasswordFile.txt')
secretPassword = passwordFile.read()
print('Enter a password: ')

typedPassword = input()
if typedPassword == secretPassword:
    print('Access granted')

    if passwordFile == '12345':
        print('He is an idiot')
else:
    print('Access denied')