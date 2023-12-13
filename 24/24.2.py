#27692
a=open("24.2.txt").readline()
p=0
count=1
for i in range(len(a)-1):
    if a[i]+a[i+1]=="BB":
       count+=1
    else:
        p=max(count,p)
        count=1
print(p)
