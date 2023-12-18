while True:
    a=int(input("Введите первый множитель-"))
    b=int(input("Введите второй множитель-"))
    c=a*b
    if len(str(c))!=3:
        print(c)
    elif len(str(c))==3:
        break
print("exit")

