a=open("17var20.txt")
b=[int(i) for i in a]
count=0
mi=10000000
for i in range(len(b)-1):
    if b[i]>300 or b[i+1]>300:
        count+=1
        mi=min(mi,b[i]**2+b[i+1]**2)
print(count,mi)
