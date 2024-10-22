# логический тип данных true false. операторы: условные , сравнения, логические.
"логич операторы or, and, not"
# print(not False)
# print(not True)


# signal = "yellow"
# if signal == "green":
#    print("GO")
# elif signal == "red":
#    print("red")
# elif signal == "yellow":
#    print("wait")
# else:
#    print("off")


"операторы сравнения"
# print(2<3 and 2 > 1)
# print(3>2>1)
# print(2<3 or 2 > 5)
# print(2<=5)


# print(2 < 5 or 2 > 5)
# print(2<=5)
# print(2==2)
# print(3 != 2)
# print(2<3)
# print(2>3)
# print(2 <= 3)
# print(2>=3)


# signal = input ("enter signal").lower()
# if signal == "green" or signal ==("зеленый"):
#    print("GO")
# elif signal == "red" or signal ==("красный"):
#    print("red")
# elif signal == "yellow" or signal ==("желтый"):
#    print("wait")
# else:
#    print("off")


# temp = int(input("введите температуру:"))

# if temp >= -30 and temp <= 0:
#   print("cold")
# elif temp >= 1 and temp <= 16:
#   print("cool")
# elif temp >= 17 and temp <= 25:
#   print("warm")
# elif temp >= 26 and temp <= 42:
#   print("too warm")
# else:
#   print("температура не соотвутствует!")


# less 1000 - low
# 1001 - 2000-mid
# 2001- greated - too much

try:
    attemps = int(input("введите кол-во попыток"))
except:
    print("ошибка, вводите только числа")
finally:
    attemps = int(input("введите кол-во попыток повторно"))
while attemps > 0:
    print(f"попытки: {attemps}")
    try:
        sum_exp = int(input("введите потраченную сумму"))
    except:
        print("ошибка, вводите только числа!")
        continue
    if sum_exp == 0:
        print("не потрачено ни одной копейки")
    elif sum_exp >= 1 and sum_exp <= 1000:
        print("деньги не превышают середины нужного бюджета")
    elif sum_exp >= 1001 and sum_exp <= 2000:
        print("деньги дошли до лимита бюджета ")
    elif sum_exp >= 2001:
        print("лимит бюджета превышен")
    else:
        print("значения введены некорректно!")
    attemps -= 1

