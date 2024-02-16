a=input("Строка-")
b=input("Нужная буква-")
if b in a:
    for i in range(len(a)):
        if b==a[i]:
            break
    for j in range(len(a)-1,-1,-1):
        if b == a[j]:
            break
    if i==j:
        print(i+1)
    else:
        print(i, j)






