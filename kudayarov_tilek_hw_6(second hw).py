value = 6
a = [6, 17, 21, 27, 32, 35, 35, 36, 37, 48]
n = len(a)
first = 0
last = n - 1
middle = n // 2
resultOK  = False

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
    print('ID =', middle)
else:
    print('No value')
