n=100
k=60
r=1
t=10



kol=[]
mx=0
a=[list(map(int,i.split(' '))) for i in open('27_A_ya.txt')]
razn=[i[0]-i[1] for i in a]

for i in range(len(a)):
    if k<=t:
        break
    print(k,a[razn.index(sorted(razn)[i])][0],a[razn.index(sorted(razn)[i])][1],razn[razn.index(sorted(razn)[i])])
    k-=a[razn.index(sorted(razn)[i])][0]
    kol.append(a[razn.index(sorted(razn)[i])][1])

print(sum(kol),'//')

print(razn[razn.index(sorted(razn)[0])],min(razn))




"""374"""