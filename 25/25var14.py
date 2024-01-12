count=0
for i in range(850000,2000000):
    mi=10000000000
    ma=0
    flag=False
    for d in range(2,int(i**0.5)+1):
        if i%d==0:
            mi=d
            ma=i//d
            flag=True
            break

    f=ma-mi
    if f%5==0 and flag:
        count+=1
        print(i,f)
    if count==6:
        break