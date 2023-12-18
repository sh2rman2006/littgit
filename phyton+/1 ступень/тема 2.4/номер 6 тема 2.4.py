n=int(input("Введите диапазон-"))
for i in range(1,n+1):
    d=0
    for h in range(1,n+1):
        if i%h==0:
            d+=1
    if d==2:
        print(i)




