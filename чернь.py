kolvo = 0
m2=[0]
ind=0
for i in range(710017,710017 * 2):
    m = 0
    maxdel = []
    for d in range(2, int(i ** 0.5) + 1):
        if i%d==0 and i**0.5!=d:
            maxdel.append(d)
    if len(maxdel)>0:
        m = max(maxdel) + i // max(maxdel)
    m2.append(m)
    if m%10==0 and m>m2[ind]:
        kolvo += 1
        ind+=1
        if kolvo < 6:
            print(i, m)
        else:
            break
    else:ind+=1




