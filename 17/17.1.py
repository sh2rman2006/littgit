a=open("17 (1).txt")
b=[]
for i in a:
    b.append(int(i))
count=0
p=-1000000
for i in range(len(b)-1):
    for y in range(i+1,len(b)):
        if (b[i]-b[y])%2==0:
            if(b[i]) % 19 == 0 or (b[y]) % 19 == 0:
                sum=b[i]+b[y]
                p=max(p,sum)
                count+=1
print(count,p)
