for i in range(106732567,152673836+1):
    k=[]
    for d in range(2,int(i**0.5)):
        if i%d==0:
            k.append(d)
            k.append(i//d)
    if i**0.5%1==0:
        k.append(int(i**0.5))
    if len(k)==3:
        print(i,max(k))