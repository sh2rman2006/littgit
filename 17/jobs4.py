a=open("17jobs.txt")
b=[int(i) for i in a]
mi=100000000000
for i in b:
    mi=min(mi,i)
count=0
sm=-100000000
for i in range(len(b)-1):
    if b[i]%117==mi or b[i+1]%117==mi:
        sv=b[i]+b[i+1]
        sm=max(sm,sv)
        count+=1
print(count,sm)


