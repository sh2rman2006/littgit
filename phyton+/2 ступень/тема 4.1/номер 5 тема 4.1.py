a=[]
Imax=Imin=0
for i in range(int(input("Количество-"))):
    a.append(int(input("Введите числа-")))
print(a)
Max=Min=a[0]
for i in range(len(a)):
    if Max<a[i]:
        Max=a[i]
        Imax=i
    if Min>a[i]:
        Min=a[i]
        Imin=i
a[Imax], a[Imin]=a[Imin], a[Imax]
print(a[::-1])
