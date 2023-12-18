parol=int(input("Введите трехзначный пароль (правильный)-"))
a=3
while a!=0:
    b=int(input("Введите пароль-"))
    if b!=parol:
        print("Неправильный пароль!")
        a -= 1
    elif b==parol:
        print("Верный пароль")
        a=0
    if b!=parol and a==0:
        print("Вы заблокированы!")




