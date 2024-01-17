kolvo = 0
for i in range(710017,710017 * 2):
    m = 0
    m2=0
    maxdel=[]
    maxdel2=[]
    for d in range(2, int(i ** 0.5)+1):
        for d2 in range(2, int((i-1) ** 0.5)+1):
            if (i-1) % d == 0 and  (i-1)**0.5!=d:
                maxdel2.append(d)
        if i%d==0 and i**0.5!=d:
            maxdel.append(d)
    if len(maxdel)>0:
        m = max(maxdel) + i // max(maxdel)
    if len(maxdel2)>0:
        m2 = max(maxdel2) + (i-1) // max(maxdel2)
    if m>m2 and m%10==0:
        kolvo+=1
        if kolvo<6:
            print(i,m)
        else:break