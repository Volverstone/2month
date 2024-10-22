#цикл for
#name = ("Tilek Kudayarov")
#for i in range(1,11):
#print(name)


#цикл while
#i = 1
#while i <= 10:
#    print(i)
#    i += 1
#    break
#break сразу делает выход из цикла ближайшего


#i = 1
#while i <= 10:
#    if i !=5:
#        print(i)
#    i+=1
#    continue
#continue пропускает одно из действий цикла


#бесконечный цикл
#i = 1
#while i == 1:
#    print("бесконечный цикл")


#a =["hello", 54 , 52.1]
#for i in a:
#    if type(i) ==int:
#        a.remove(i)
#print(a)

#Операторы принадлежности назначения циклы

#операторы назначения = += -= /= *=...
#number = 10
#number = number + 5
#number += 5
#number -= 3
#number *= 2
#number /= 2
#print (number)

#оператор принадлежности
#word = "geeks"
#print("o" in word)
#print("e" in word)
#print(32 in (1,54))
#print(0.2) in (1, 100))

#counter = 0
#while counter<1000:
#    counter += 1
#
#    if counter == 500:
#        print("exit")
#        break
#
#    if counter % 2 == 0:
#        print("number ignored")
#        continue
#    print("geeks", counter)

numbers = range(1, 21)
for number in numbers:
    print(number)

word = "kyrguzstan"
for letter in word:
    print(letter)

word = "kyrguzstan"
for letter in word:
    if letter == "s":
        break
    print(letter)

word = "kyrguzstan"
for letter in word:
    if letter in "gzs":
        continue
    print(letter)

