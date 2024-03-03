for x in range(19):
    a=[7,8,x,7,9,6,4,3]
    b=[2,5,x,4,3]
    c=[6,3,x,5]
    for i in range(len(a)):
        a[i]=a[i]*19**(len(a)-1-i)
    for i in range(len(b)):
        b[i]=b[i]*19**(len(b)-1-i)
    for i in range(len(c)):
        c[i]=c[i]*19**(len(c)-1-i)
    a=sum(a)
    b=sum(b)
    c=sum(c)
    if (a+b+c)%18==0:
        print((a+b+c)//18)
        break