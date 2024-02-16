a=[]
for i in range(int(input("Количество-"))):
    a.append(int(input("Введите числа-")))
print(a)
for i in range(len(a)):
    if a[i] not in a[:i]+a[i+1:]:
        print(a[i])
