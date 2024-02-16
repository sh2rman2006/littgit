n=int(input(" Введите количество-"))
x = input(" Введите число-")
for i in range(n):
    a=input("Введите число-")
    s=0
    for h in a:
        if h==x:
            s+=1
    print(s)



