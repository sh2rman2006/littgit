a=[]
for i in range(int(input("Элементов в списке-"))):
    a.append(int((input("Введите числа-"))))
for i in a:
    if i%2==0:
        print(i)
    elif i==237:
        break

