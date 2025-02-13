import random


def start_game(min_number, max_number, attempts, initial_capital):
    capital = initial_capital

    for attempt in range(attempts):
        print(f"Попытка {attempt + 1}/{attempts}. Ваш капитал: {capital}")

        if capital <= 0:
            print("Ваш капитал исчерпан. Игра завершена!")
            break


        bet = int(input(f"Введите ставку: "))
        if bet > capital:
            print("У вас недостаточно капитала для этой ставки.")
            continue


        guess = int(input(f"Введите число от {min_number} до {max_number}: "))

        number_to_guess = random.randint(min_number, max_number)
        print(f"Загаданное число: {number_to_guess}")


        if guess == number_to_guess:
            print("Поздравляем! Вы угадали число!")
            capital += bet
        else:
            print("Увы, вы не угадали число.")
            capital -= bet


        if capital <= 0:
            print("Ваш капитал исчерпан. Игра завершена!")
            break

    print(f"Игра завершена. Ваш окончательный капитал: {capital}")
