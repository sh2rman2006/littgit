#27690
a=open("24.1.txt").readline()
count=1
p=0
for i in range(len(a)-1):
    if a[i]!=a[i+1]:
        count+=1
    else:
        p=max(count,p)
        count=1
print(p)
