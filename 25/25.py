for i in range(174457,174506):
    c=0
    a=[]
    for d in range(2,int(i**0.5)):
        if i%d==0:
            c+=2
            if c>2:
                break
    if i**0.5%1==0:
        c+=1
    if c==2:
        for d in range(2, int(i ** 0.5)):
            if i%d==0:
                print(d,i/d,i)








