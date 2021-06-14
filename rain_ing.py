# coding practice by following flowchart.


# first print a greetings.

print('Good mornings guys !!')

# make an if else for raining or not

is_raining = input('Is it raining outside ? ').upper()

if is_raining == 'YES':

    print('Do you have an umbrella ?')

    have_umbrella = input('Do you have umbrella ? ').upper()

    if have_umbrella == 'YES':
        print('Go outside !')
    else:
        print('Wait a while!!')
        print('Till its not raining!')



else:
    print('Go outside and enjoy the sun shine!!')

print('End')
