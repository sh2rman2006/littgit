count=0
for i in open('9_yasl1.csv'):
    a=list(map(int,i.split(',')))
    rp=[i for i in a if a.count(i)==2]
    if len(rp)==6:
        rp.sort()
        if ((rp[0]**2+rp[2]**2)**0.5)==max(rp):
            count+=1
print(count)
