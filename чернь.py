kolvo = 0
m2=[]
for i in range(710017,710017 * 2):
    m = 0
    maxdel = []
    for d in range(2, int(i ** 0.5) + 1):
        if i%d==0 and i**0.5!=d:
            maxdel.append(d)
    if len(maxdel)>0:
        m = max(maxdel) + i // max(maxdel)

