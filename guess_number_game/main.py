from decouple import config

import random
from logic import start_game

min_number = int(config('MIN_NUMBER'))
max_number = int(config('MAX_NUMBER'))
attempts = int(config('ATTEMPTS'))
initial_capital = int(config('INITIAL_CAPITAL'))


def main():
    print(f"Добро пожаловать в игру 'Угадай число'!")
    print(f"Вы должны угадать число от {min_number} до {max_number}. У вас {attempts} попыток.")
    print(f"Ваш начальный капитал: {initial_capital}")

    start_game(min_number, max_number, attempts, initial_capital)


if __name__ == "__main__":
    main()
