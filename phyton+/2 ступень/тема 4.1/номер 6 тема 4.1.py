a=[]
for i in range(int(input("Количество-"))):
    a.append(input("Введите числа-"))
Imax=Imin=0
Max=Min=a[0]
for i in range(len(a)):
    if Max<a[i]:
        Max=a[i]
        Imax=i
print(max(a),Imax)










