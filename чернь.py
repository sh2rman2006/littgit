b=[int(i) for i in open('8 60 1 40.txt')]
count=0
for i in range(len(b)):
    for k in range(i+1,len(b)):
        if (b[i]*b[k])%7==0 and (b[i]+b[k])%2==0 and abs(b.index(b[i])-b.index(b[k]))>=4:
            count+=1
            print(b[i],b[k])
print(count)
