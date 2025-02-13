def guess_number():
    upper = 100
    lower = 1
    attemps = 0
    attemps_list = []
    print('загадайте число от 1 до 100')
    while True:
        attemps +=1
        guess = (lower + upper) // 2
        attemps_list.append(guess)
        print(f'я думаю что это {guess}')
        response = input("введите больше или меньше или да")
        if response == 'да':
            with open('results.txt', 'w') as file:
                file.write(f'Количество попыток: {attemps}\n'
                           f'Список попыток{attemps_list}\n'
                           f'искомое число{attemps_list[-1]}')
            break
        elif response == 'меньше':
            upper -= 2
        elif response == 'больше':
            lower += 2
        else:
            print('Некорректный ввод, введите только меньше больше или да')
            continue


guess_number()


