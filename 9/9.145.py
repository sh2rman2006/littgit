count=0
for i in open("9.145.csv"):
    a=list(map(int,i.split(";")))
    rep=[i for i in a if a.count(i)==2]
    nrp=[i for i in a if a.count(i)==1]
    ch = []
    nch = []
    for k in a:
        if k % 2 == 0:
            ch.append(k)
        if k % 2 != 0:
            nch.append(k)
    ch1 = 0
    nch1 = 0
    if len(ch) > 0:
        ch1 = sum(ch) / len(ch)
    if len(nch) > 0:
        nch1 = sum(nch) / len(nch)
    if ((len(rep)==2 and len(nrp)==4) and(not abs(ch1 - nch1) > 50)) or ((not(len(rep)==2 and len(nrp)==4))and(abs(ch1-nch1)>50)):
        count+=1
print(count)



