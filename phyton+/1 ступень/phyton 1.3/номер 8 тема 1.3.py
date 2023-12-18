a=input("Введите трехзначное число-")
Mi=min(int(a[0]),int(a[1]),int(a[2]))
Ma=max(int(a[0]),int(a[1]),int(a[2]))
ost=sum([int(a[0]),int(a[1]),int(a[2])])-(Ma+Mi)
if sum([Mi,Ma])/2==ost:
    print("Вы ввели иентересное число!")
else:
    print("вы ввели обычное число!")


