for n in range(1,100000):
    r=bin(n)[2:]
    if n%8==0:
        r+=r[:2]
    else:
        r+=bin((n%8)*2)[2:]
    if int(r,2)>=3000:
        print(n)
