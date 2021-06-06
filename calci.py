print('Basic calculator')
while True:
    first_no = float(input('First no: '))
    operator = input('Operator: ')
    second_no = float(input('Second no: '))
    if operator == '+':
        print(f'Answer: {first_no + second_no}')
    elif operator == '-':
        print(f'Answer: {first_no - second_no}')
    elif operator == '*':
        print(f'Answer: {first_no * second_no}')
    elif operator == '/':
        print(f'Answer: {first_no / second_no}')
    else:
        print('invalid operator')