count=0
for i in open('09statgr.csv'):
    a=list(map(int,i.split(';')))
    rp=[i for i in a if a.count(i)>1]
    if len(rp)>0 and a.count(max(a))==1 and sum(rp)>max(a):
        count+=1
print(count)