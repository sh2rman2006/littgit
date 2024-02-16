n=int(input("Количество элементов в списке-"))
a=[]
for i in range(n):
    a.append(int(input(str(i+1)+" Введите число-")))
m=int(input("Введите м-"))
for i in a:
    if i > m:
        print("Больше м-",i)

