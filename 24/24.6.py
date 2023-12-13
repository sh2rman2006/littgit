a=open("24.6.txt").readline()
ma=0
count=0
for i in range(len(a)):
    if (a[i]=="A" and count%2==0) or (a[i]=="B" and count%2==1):
        count+=1
    else:
        ma=max(ma,count)
        count=0
print(ma)

