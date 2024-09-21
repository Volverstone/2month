import EXAMEN_tilek_K as exam_db
connect_to_db = exam_db.create_connection('''examen.db''')

while True:
    print("""Вы можете отобразить список продуктов по выбранному id 
города из перечня магазинов выше, для выхода из программы введите цифру 0:""")
    exam_db.store_print(connect_to_db)
    add = int(input("ВВОД:"))

    if add == 0:
        print("ВЫХОД")
        break
    else:
        pr = exam_db.all_print(connect_to_db,add)
        pr = list(pr)
        print(f'Название продукта: {pr[0]}\n'
              f'Категория:{pr[1]}\n'
              f'Цена:{pr[2]}\n'
              f'Кол - во на складе:{pr[3]}')
