# 2#Cловари и множества
#
# """из чего состоит словарь  """
# # #{key : value}
# # student = {}
# # print (student)
# # print(type(student)) # class dict - dictionary
#
# #student2 = dict(name="aliya", age=21, country= "KZ", weight=56.2)
#
#
# student = {
#     "name": "Adilet",
#     "age":19
# }
# print(student)
# print(student["age"]) #выводит значения ключа age
# #
# # """словарь можно изменять и добовлять     """
# # #в словарь можно добавить все типы данных в виде значений ключей
# # student["height"] = 1.77
# student["married"]=False
# student["hobby"] = ["english","books","chess"]
# student["education"] = ("english","school","college")
# """редактирование  """
# student["age"] += 1
# student["hobby"][-1]="football"
# """удаление"""
# student["hobby"].pop(-1) #мы удалили элемент под индексом -1 из списка hobby
# del student["married"]
# #student.update(student2)
# #print(student2)
# print(student.get("nam","неверный ключ")) # выводит неверный ключ тк у нас нет ключа nam
# #.items #возваращет обьекты по парам: ключ, знач-е ключа
# for key, value in student.items():
#     print(f"{key}: {value}")
# for i in student:
#     print(i, student[i])
# print(student)
# numbers= [1,2,3,2,4,1,3,5,]
# numbers2 = {1,2,3,2,4,1,3,5,}
# print(numbers)
# print(numbers2)
# beshbarmak = {"мясо","тесто","лук"}
# plov = {"рис","мясо","морковь"}
# print(beshbarmak.union(plov))
# print(beshbarmak.difference(plov))
# print(beshbarmak.intersection(plov))
# print(beshbarmak.symmetric_difference(plov))
from random import choice
topics = tuple(range(1,7+1))
students = [16,18,9,2,7,5,19,12,21,16,11,8,10,20,17,13]
database = {}

while students:
    print(students)
    choisen_student = choice(students)
    name = input(f"student: {choisen_student} enter name:").title()
    rate = int(input(f"topic {choice(topics)} enter rate for {name}:"))
    database[name] = rate
    students.remove(choisen_student)
for name, rate in database.items():
    print(f"{name}: {rate}")