def binary_search(a,value):
    n = len(a)
    first = 0
    last = n - 1
    middle = n // 2
    resultOK = False
    while a[middle] != value and first <= last:
        if value > a[middle]:
            first = middle + 1
        else:
            last = middle - 1
        middle = (first + last) // 2
    if value == a[middle]:
        resultOK = True

    if resultOK == True:
        #ID Это индекс элемента в списке
        print(f"ID of {value} == {middle}")
    else:
        print('No value')
lst = [6, 17, 21, 27, 32, 35, 35, 36, 37, 48]
print(lst)
binary_search(lst,35) #значение найдено
binary_search(lst,11) #значение не найдено, его нет в списке