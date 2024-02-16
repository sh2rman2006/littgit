n=int(input("-"))
a=[]
b=[]
for i in range(n):
    a.append(int(input(str(i+1)+":a-")))
for j in range(n):
    b.append(int(input(str(j+1)+":b-")))
a=map(lambda i,j:(i**2)+(j**2), a, b)
print(*a)




