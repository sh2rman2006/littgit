for i in range(2,17):
    m=0
    count=0
    for d in range(2,int(i**0.5)+1):
        if i%d==0:
            m=m+d+i//d
    if i**0.5%1==0:
        m-=int(i**0.5)
    print(i,m)