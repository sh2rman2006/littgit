k=0
for i in open("9.1.csv"):
    a=list(map(int,i.split(";")))
    repeat=[int(x) for x in a if a.count(x)==2 or a.count(x)==4]
    if len(repeat) ==4 and (max(repeat )+min(repeat))==180:
        k+=1
print (k)



