a=[]
n=int(input("строки-"))
m=int(input("столбцы-"))
for i in range(n):
    a.append([])
    for h in range(m):
        a[i].append(input("["+str(i+1)+","+str(h+1)+"]-"))
print(a)
for i in a:
    for k in i:
        print(k, end=" "*(5-len(str(k))))
    print()







