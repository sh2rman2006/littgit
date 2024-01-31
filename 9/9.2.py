count=0
for i in open("9.2.csv"):
    a=list(map(int,i.split(";")))
    rep=[int(x) for x in a if a.count(x)==2]
    net=[int(x) for x in a if a.count(x)==1]
    if len(rep)==6 and (max(rep)+min(rep))/2<net[0]:
        count+=1
print(count)
print("исходник")
