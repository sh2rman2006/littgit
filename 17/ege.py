a=open("ege.txt")
b=[int(i) for i in a]
maxb=-100000000
for i in b:
    if len(str(i))==5 and str(i)[-1]=="3":
        maxb = max(maxb, i)
count=0
maxsum=0
for i in range(len(b)-2):
    m=0
    if str(b[i])[-1]=="3" or str(b[i+1])[-1]=="3" or str(b[i+2])[-1]=="3":
        m=b[i]+b[i+1]+b[i+2]
        if m<maxb:
            count+=1
            maxsum=max(maxsum,m)
print(count,maxsum)