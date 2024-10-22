#функции(ч.1) виды параметров. возвращение данных. виды документов
#DRY - dont repeat yourself
#def - defind

"""схема функции"""
#определение наименованния(параметры)
#тело функции
#возвращение результата
#
#вызов функции
#наименование(аргументы)
def get_square(width: int, length: int):
    """принимает в себя длину и ширину, возвращает площадь квадрата или 
    прямоуголника"""
    square = width * length
    return square

print(get_square.__doc__)
print(help(get_square))
square_2 = get_square(5, 7)
square_hall = get_square(15, 10 )
print(square_2)
print(square_hall)



def get_data(name,surname="неизвестно"):
    print(f"name {name.title()} surname {surname.title()}")
get_data(name=" azamat", surname=" musagaliev")
get_data("mike","tyson")
get_data("peter")
get_data("leo", "messi")




expenses = 0
for day in range(1,8):
    print(expenses)
    expenses += int(input(f"enter expenses, {expenses}"))
    
print(expenses)
print()





