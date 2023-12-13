b=open("17.3.txt")
a=[]
mi=100000000
for i in b:
    if int(i)%21==0:
        mi=min(mi,int(i))
    a.append(int(i))
ma=-10000000000
count=0

for i in range(len(a)-1):
    sum=a[i]+a[i+1]
    if (a[i]%mi==0 or a[i+1]%mi==0):
       count+=1
       ma=max(ma,sum)
print(count,ma)