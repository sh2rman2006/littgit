#27696
a=open("24(5).txt").readline()
count=1
ma=0
for i in range(len(a)-1):
    if a[i]+a[i+1]=="LL":
        count+=1
    else:
        ma=max(ma,count)
        count=1
print(ma)




