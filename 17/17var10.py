a=open("17var10.txt")
b=[int(i) for i in a]
sm=10000000000
count=0
for i in range(len(b)-1):
    k=0

    if (abs(b[i])**(0.5)%1==0 and b[i]>0) or (abs(b[i+1])**(0.5)%1==0 and b[i+1]>0):
        k+=1
    if k>0:
        sm=min(b[i]+b[i+1],sm)
        count+=1
print(sm,count)

