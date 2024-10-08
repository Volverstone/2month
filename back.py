while True:
    n1 = float(input('введите первое число'))
    action = input('введите действие')
    n2 = float (input('введите второе число'))

    if action ==  '+':
        answer = n1 +n2
        print(answer)

    elif action == '-':
        answer = n1 - n2
        print(answer)

    elif action == '*':
        answer = n1 * n2
        print(answer)

    elif action == '/' and n2 == 0:
        print('ERROR!!!!!!!!')

    elif action == '/':
        answer = n1 / n2
        print (answer)

    else:
        print('ERROR!!!!!!!!')