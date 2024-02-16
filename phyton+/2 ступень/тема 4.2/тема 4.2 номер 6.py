n=int(input("рядов-"))
m=int(input("мест-"))
a=[]
for i in range(n):
    a.append([])
    for h in range(m):
        a[i].append(int(input("в ряду"+str(i+1)+" места-")))
print(a)
print("Вводить 1 если место занято, если не занято 0")
k=int(input("соседние свободные места в ряду-"))
for i in range(n):
    s = 0
    for h in range(m):
        if a[i][h]==0:
            s+=1
        else:
            s=0
        if s==k:
            break
    if s == k:
        break
if s==k:
    print(i+1)
else:
    print(0)






