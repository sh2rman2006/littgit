a=open("24var18-20.txt").readline()
count=1
ma=-10000000
a=a.replace("\n","")
for i in range(len(a)-1):
    if int(a[i])<int(a[i+1]):
        count+=1
    else:
        ma=max(ma,count)
        count=1
print(ma)