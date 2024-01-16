b=[str(i**3) for i in range(5,10)]
print(b)

for i in range(10**9+1,10**8,-1):
    count=0
    m=[]
    for d in range(2,int(i**0.5)):
        if i%d==0:
            count+=2
            m.append(i//d)
    if i**0.5%1==0:
        count+=1
    count+=2
    if str(count) in b:
        print(i,max(m))


