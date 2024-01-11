a=open("17var14.txt")
b=[int(i) for i in a]
mi=1000000000
count=0

for i in range(len(b)-1):
    if str(b[i])[-1]=="7" and str(b[i+1])[-1]=="7":
        count+=1
        mi=min(mi,abs(b[i]-b[i+1]))
print(mi,count)

