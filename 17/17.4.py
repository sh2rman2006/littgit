b=open("17 (4).txt")
a=[]
mi=100000000000000
for i in b:
    a.append(int(i))
for i in range(len(a)):
    if len(str(a[i]))==3 and str(a[i])[-1]=="5":
        mi=min(mi,a[i])
p=-1000000000000000000
count=0
for i in range(len(a)-1):
    if len(str(a[i]))==4 and len(str(a[i+1]))!=4:
        sum = a[i] ** 2 + a[i + 1] ** 2
        if sum % mi == 0:
            p=max(p,sum)
            count+=1
    elif len(str(a[i]))!=4 and len(str(a[i+1]))==4:
        sum=a[i]**2+a[i+1]**2
        if sum%mi==0:
            p = max(p, sum)
            count+=1
print(count,p)