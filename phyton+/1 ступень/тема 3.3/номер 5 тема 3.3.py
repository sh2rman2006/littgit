m=int(input("число строк-"))
n=int(input("ограничитель-"))
for i in range(m):
    a=input("строка-")
    if len(a)<=n:
        print(a+"*"*(n-len(a)))
    else:
        print(a[:n])
