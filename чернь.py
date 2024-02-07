count=0
ch="24680ace"
nch="13579bdf"
for n in range(1,100001):
    a=hex(n)[2:]
    b=list(a)
    c=set(b)
    if len(a)==4 and len(c)==4:
        k=k1=0
        sm=sm1=0
        for i in a:
            if i in nch:
                k1+=1
                sm+=int(i,16)
            if i in ch:
                k+=1
                sm1 += int(i, 16)
        if (k>1 and k1>1) and sm==sm1:
            count+=1
print(count)
