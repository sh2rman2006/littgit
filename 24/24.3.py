#27699
a=open("24.3.txt").readline()
p=0
count=0
for i in range(len(a)):
    if (a[i]=="L" and count%3==0) or(a[i]=="D" and count%3==1) or (a[i]=="R" and count%3==2):
        count+=1
    else:
        p=max(count,p)
        count=0
print(p)