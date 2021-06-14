while True:
    print('Who are you ?')

    name = input().lower()

    if name != 'joi':
        continue
    print('Hello Joi! Give password!!')
    password = int(input())
    if password == 12345:
        break
print('Access Granted')