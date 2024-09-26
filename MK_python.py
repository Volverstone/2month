mentors = ["Тимур", "Арсен", "Гулина", "Даниель"]
while True:
    team = input("Выберите команду (Добавить, Изменить, Удалить или выход): ").lower()
    if team == "добавить":
        if len(mentors) <= 10:
            print("Вы выбрали команду 'Добавить'")
            nam = input('Введите имя ментора: ')
            if len(nam) < 15:
                if nam in mentors:
                    print('Выбранный имя уже существует')
                else:
                    mentors.append(nam.title())
                    print(mentors)
                    continue
            else:
                print('Имя ментора не должно быть более 15 символов')
        else:
            print('Список переполнен')


# """Команда изменить"""
    elif team == "изменить":
        print("Вы выбрали команду 'Изменить'")
        print("Доступные менторы:", mentors)
        old_name = input("Введите имя ментора для изменения: ").title()

        if len(old_name) < 15:
            if old_name in mentors:
                new_name = input("Введите новое имя: ").title()
                if new_name not in mentors:
                    index = mentors.index(old_name)
                    mentors[index] = new_name
                else:
                    print("новое имя ужее есть в списке")

            else:
                print('Имени нет в списке')
        else:
            print('Имя ментора не должно быть более 15 символов')

# """удалить """

    elif team == "удалить":
            while True:
                print("Выберите способ удаления:")
                print("1. Удаление по значению")
                print("2. Удаление по индексу")

                del_way = int(input("Введите способ удаления: "))
                print("Доступные менторы:", mentors)
                if del_way == 1:
                    del_mentor = input("Введите имя ментора, которого хотите удалить: ").title()
                    if del_mentor in mentors:
                        mentors.remove(del_mentor)
                        print("Ментор удален.")
                    else:
                        print("Данного ментора нет в списке")
                    break
                elif del_way == 2:
                    if mentors:
                        index_mentor = int(input("Введите индекс ментора, которого хотите удалить: "))
                        if 0 <= index_mentor < len(mentors):
                            del mentors[index_mentor]
                            print("Ментор удален")
                            break
                        else:
                            print("Некорректный индекс")
                    else:
                        print("Список менторов пуст")
                else:
                    print("Некорректный выбор")

# """выход"""

    if team == "выход":
        print("Выход из программы.")
        break

