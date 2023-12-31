a=open("24var09-12.txt").readline()
count=0
ma=-100000000
for i in range(len(a)-2):
    count+=1

    if( a[i]+a[i+1]+a[i+2])=="000":
        count+=1
        ma=max(ma,count)
        count=0
print(ma)







