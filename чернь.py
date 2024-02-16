
for n in range(100000,1000001):
    s=set(list(str(n)))
    if len(s)==6:
        l=list(map(int,str(n)))
        l.sort()
        l=l[::-1]
        p=sum([l[i]**2 for i in range(len(l)) if i%2==0])
        print(n,p)
        input()




