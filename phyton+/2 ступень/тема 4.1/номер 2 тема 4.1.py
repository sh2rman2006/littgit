n=int(input("Элементов в 1 списке-"))
m=int(input("Элементов в 2 списке-"))
a=[]
b=[]
for i in range(n):
    a.append(input(str(i+1)+" в 1 список-"))
for i in range(m):
    b.append(input(str(i+1)+" в 2 список-"))
for i in a:
    if i in b:
        print(i, end=" ")

