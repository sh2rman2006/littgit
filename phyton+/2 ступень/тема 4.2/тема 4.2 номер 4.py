a=[]
n=int(input("списков-"))
m=int(input("элементов-"))
for i in range(n):
    a.append([])
    for g in range(m):
        a[i].append(int(input("["+str(i+1)+","+str(g+1)+"]-")))
s=0
ma=0
mi=0
p=1
for i in a:
    for g in i:
        s+=g
        p*=g
print("сумма",s,"произведение",p, end=" ")
mi=p
for i in range(n):
    for g in range(m):
        if a[i][g]>ma:
            ma=a[i][g]
        if a[i][g]<mi:
            mi=a[i][g]
print("максимум",ma,"минимум",mi)

