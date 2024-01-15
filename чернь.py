for i in range(1273547,1273547*5):
    m=0
    count=0
    for d in range(2,int(i**0.5)+1):
        if i%d==0:
            m=m+d+i//d
    if i**0.5%1==0:
        m-=int(i**0.5)
    ost=m%100000
    if m>0:
        for ostdel in range(2,int(m**0.5)+1):
            if ost%ostdel==0:
                break
            if ost ** 0.5 % 1 == 0:
                break
        else:
            print(i,m)





