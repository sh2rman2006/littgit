count=0
for i in open("9.valera.csv"):
    a=list(map(int,i.split(";")))
    rep=[i for i in a if a.count(i)==3]
    notrp=[i for i in a if a.count(i)==1]
    b=a.copy()
    b.sort()
    if (len(rep)==3 and len(notrp)==4) and a==b:
        count+=1
print(count)


