#списки и кортежи. Индексы и СРезы. Встроенные функции к наборам элементов.

# numbers = [10, 7, 1, 5, 3, 11, 8, 6 ,4, 6.3 , 5.5 , 3.5 , 2.5, 0.8]
#
# print(numbers)
# print(numbers[9:])
# print(numbers[-5:])
# print(numbers)
# """ схема генерации списка(спимскового включения) """
# numbers2 = [number for number in numbers if number < 5]
# print(numbers2)
# students = ("dastan","janadil", "atayan", "fatima", "dastan")
# print(students)
# print(type(students))
numbers = (45)#обычная int переменная
numbers = (45,)# кортеж! там есть запятая


#что такое list comperhension в питон, узнать и
# print(numbers)
# print(min( numbers))
# print(max(numbers))
# print(sum(numbers))
# print(sorted(numbers, reverse=True))

# students = ["azim", "samat", "tilek", "vasya","petya","vlad"]
# students2 = [student.title() for student in "a" in students ]
# print(students)
# print(students2)
# new_copy = students.copy()
# print(new_copy)
#
# new_copy[0] = "erkin"
# print(new_copy)
# print(students)
# print(students == new_copy)# проверка на схожесть значений списков двух перменных
# print(id(students))
# print(id(new_copy))
# print(students is new_copy)
#
# print(students.index("azim"))# индексы значений в списке
# print(students.count("tilek"))# cколько раз встречается в списке
# print(students[1].count("a"))

# print (len(students))
# print (sorted(students))
#"""индексы и срезы"""
#ИНДЕКСЫ
#print(students[0])
#print(students[2])
#print(students[-1])
#print(students[-3])

#CРЕЗЫ
#схема среза - [start:stop:step]
#print(students[1:3]) # с 1  по 3 не включительно(т.е. 2)
#print(students[2:4]) # со 2 по 4 не включительно(т.е. 3)
#print(students[2:]) #от 2 индекса до конца
#print(students[:2]) #от начала индекса до 2 индекса не включительно
#print(students[::2]) #каждый второй индекс
#print(students[::-1])

"""add"""
#3 метода
# students.append("adina")
# students.insert(1,"dastan")
# students.extend(["atai","yaroslav","janadyl"])
# students+= ["vlad","mark","atayan"]
# print(students)
# """edit"""
# students[4] = "maksat"
# students[:3] = ["malik", "bakyt", "jack"]
# print(students)
# students[2:5] = students[2:5][::-1]#реверс от 2 до 4 индекса
# students.sort(reverse=True)#сортировка от конца до начала
# print(students)
#
# """delete"""
# students.remove("malik") # remove удаляет ТОЛЬКО по названию обьекта и полностью его удаляет
# deleted = students.pop(0) #pop удаляет по ИНДЕКСУ и ВЫРЕЗАЕТ  индекс и хранит его где то
# del students [1:4] #del - универсален! он может много индексов удалять или 1
# #del students [-1]
# print(students)
# print(deleted)
#
