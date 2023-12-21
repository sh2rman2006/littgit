for k in range(1,10000000):
    n=1850000000+k
    ch=0
    for d in range(2,n//2+1,2):

        if n%d==0:
            if d%2==0:
                ch+=1
    if ch%2!=0:
        print(k)

