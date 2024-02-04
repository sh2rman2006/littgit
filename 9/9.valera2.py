count=0
sm=0
for i in open("9.valera.csv"):
    count+=1
    a=list(map(int,i.split(";")))
    rep=set(a)
    if a==sorted(a) or len(rep)<5:
        sm+=count
print(sm)