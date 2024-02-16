n=int(input("Введите диапазон-"))
a=int(input("введите количество делителей-"))
for i in range(1,n+1):
    d=0
    for h in range(1,n+1):
        if i%h==0:
            d+=1
    if d==a:
        print("число", i, "имеет делителей-",a)



