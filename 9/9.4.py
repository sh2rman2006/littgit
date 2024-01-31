c=[]
d=0
for i in open("9.4.csv"):
    a=list(map(int,i.split(";")))
    rep=[x for x in a if a.count(x)==2]
    net=[x for x in a if a.count(x)==1]
    if (len(net)==4 and len(rep)==4)and (min(a) in net):
        for k in a:
            c.append(k)
            d+=k
print(d/len(c))