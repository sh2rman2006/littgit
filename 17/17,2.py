b=open("17 (2).txt")
a=[]
for i in b:
    a.append(int(i))
p=-10000000000000
count=0
for i in range(len(a)-1):
    for y in range(i+1,len(a)):
        sum=a[i]+a[y]
        if sum%80==0 and (a[i]%50==0 or a[y]%50==0):
            count+=1
            p=max(p,sum)
print(count,p)
