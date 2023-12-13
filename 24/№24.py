"""a=open("24_demo.txt").readline()
count=1
p=0
for i in range(len(a)-1):
    if a[i]!=a[i+1]:
        count+=1
    else:
        p=max(count,p)
        count=1
print(p)
"""
#2
"""a=open("24_demo.txt").readline()
count=1
p=0
for i in range(len(a)-1):
    if a[i]+a[i+1]=="XX":
        count+=1
    else:
        p=max(count,p)
        count=1
print(p)"""
#5
a=open("24_demo (1).txt").readline()
count=0
p=0
for i in range(len(a)-1):
    if (a[i]=="X" and count%3==0) or (a[i]=="Y" and count%3==1) or (a[i]=="Z" and count%3==2):
        count+=1
    else:
        p=max(count,p)
        count=0
print(p)





