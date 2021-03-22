raining = input('Is it raining outside ? ')

if raining == 'YES':
    umbrella = input('Do you have any umbrella ? ')
    if umbrella == 'YES':
        print('Go Outside.!')
    elif umbrella == 'NO':
        print('Wait For a while')
elif raining == 'No':
    print('Go outside!')
else:
    print('It is sunny !')