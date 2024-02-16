while True:
    al=input("Введите действие-")
    if al=="x":
        print("exit")
        break
    if al=="n!":
        c=int(input(" Введите число-"))
        d=1
        for i in range(1,c):
            print(i*d)
    a=int(input("Введите число-"))
    b=int(input("Введите число-"))
    if al=="+":
        print(a+b)
    if al=="-":
        print(a-b)
    if al=="/" and b!=0:
        print(a/b)
    if al=="/" and b==0:
        print("Деление на ноль!")
    if al=="//" and (a//b)==0:
        print(a//b)
    if al=="//" and b==0:
        print("Деление на ноль!")
    if al=="//" and (a//b)!=0:
        print("Нет целочисленного деления!")
    if al=="%" and (a%b)==0:
        print(a%b)
    if al=="%" and b==0:
        print("Деление на ноль!")
    if al=="**":
        print(a**b)