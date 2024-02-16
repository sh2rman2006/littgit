a=input("-").split()
b=[]
for i in range(len(a)):
    if a.count(a[i])==1:
        b.append(a[i])
print(b[::-1])
a=tuple(b[::-1])
print(a)