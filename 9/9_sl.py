sm=0
for i in open("9_sl.csv"):
    a=list(map(int,i.split(";")))
    rep1=[i for i in a if a.count(i)==3]
    rep2=[i for i in a if a.count(i)==2]
    if len(rep1)==3 and len(rep2)==4:
        mn=[]
        for k in sorted(a):
            if len(mn)==4:
                break
            mn.append(k)
        komb=[i for i in mn if i%2==0]
        if len(komb)==2:
            sm+=sum(a)
print(sm)