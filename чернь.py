for i in range(1,10**9):
    count=0
    for d in range(1,int(i**0.5)):
        if i%d==0:
            count+=2
    if i**0.5%1==0:
        count+=1
    if count < 125:
        continue
    elif len(str(count))==3 and count**(1/3)%1==0:
        print(i)