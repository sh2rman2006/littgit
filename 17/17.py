a=open("17.txt")
b=[]
for i in a:
    b.append(int(i))

count=0
p=-100000
for i in range(len(b)-1):
    if (b[i])%3==0 or (b[i+1])%3==0:
        count+=1
        sum=b[i]+b[i+1]
        p=max(p,sum)
print(p,count)





