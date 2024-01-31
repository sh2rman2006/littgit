count=0
for i in open("9.5.csv"):
    a=list(map(int,i.split(";")))
    sm=(max(a)+min(a))**2
    s=[i for i in a if i!=max(a) and i!=min(a)]
    s1=0
    for k in s:
        s1+=k
    if sm>s1:
        count+=1
    print(a,s)
    print("////")
    print(sm,s1,end="\n")
print(count)
