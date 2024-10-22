 #обработка исключений. Тест
"схема обработки исключений"
#try:
#    попытаемся найти ошибкy
#except:
#    обработка запроса
#finally:
 #   выдает сообщение о завершении проверки
try:
    print(2 + "ewf131")
except:
    print("ошибка, что то не так")
finally:
    print("проверка завершена")


while True:
    answer = input("enter number or exit")
    if answer == "exit":
        break
    try:
        answer = int(answer)
        print(word[answer])
    except ValueError:
        print("add only numbers")
    except IndexError:
        print("your number is too big!")