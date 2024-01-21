a=open("17_10100.txt")
maxz=0
b=[int(i) for i in a]
for i in b:
    if str(i)[-2:]=="13":
        maxz=max(maxz,i)

count=0
ma=-100000000
for i in range(len(b)-2):
    k=0
    if len(str(b[i]))==3:
        k+=1
    if len(str(b[i+1]))==3:
        k+=1
    if len(str(b[i+2]))==3:
        k+=1
    if k==3 and (b[i]+b[i+1]+b[i+2])<=maxz:
        count+=1
        ma=max(ma,b[i]+b[i+1]+b[i+2])
print(count,ma)
