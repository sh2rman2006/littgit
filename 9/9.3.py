al=0
for i in open("9.3.csv"):
    a=list(map(int,i.split(";")))
    rep3=[x for x in a if a.count(x)==3]
    rep2=[x for x in a if a.count(x)==2]
    if len(rep2)==4 and len(rep3)==3:
        d=sorted(a)
        mas=[d[0],d[1],d[2],d[3]]
        sm=[mas[x]+mas[x+1] for x in range(len(mas)-1) if (mas[x]+mas[x+1])%2!=0]
        if len(sm)==2:
            for i in a:
                al+=i
print(al)



