print ('-' * 32)
print ('Welcome to the online calculator')
print ('-' * 32)

begin = int(input('Start? [1] Yes [2] No\n'))

while begin < 1 or begin > 2:
    begin = int(input('Please enter a valid number [1] Yes [2] No\n'))

while begin == 1:
    first_choice = float(input('Please enter the first number.\n'))
    second_choice = float(input('Please enter the second number.\n'))
    operator = int(input('Now choose the operator.\n[1] add [2] sub [3] mult [4] div\n'))
    
    while operator < 1 or operator > 4:
        print('Please enter a valid operator')
        operator = int(input('[1] sum [2] div [3] sub [4] mult\n'))
    
    if operator == 1:
        print(f'{first_choice} + {second_choice} = {first_choice + second_choice}')
    
    elif operator == 2:
        print(f'{first_choice} - {second_choice} = {first_choice - second_choice}')
    
    elif operator == 3:
        print(f'{first_choice} * {second_choice} = {first_choice * second_choice}')

    else:
        print(f'{first_choice} / {second_choice} = {first_choice / second_choice}')
    
    begin = int(input('Restart? [1] Yes [2] No\n'))
    
    while begin < 1 or begin > 2:
        begin = int(input('Please enter a valid number [1] Yes [2] No\n'))

print('Goodbye')
