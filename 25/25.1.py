#27850

k=0
for i in range(245690,245756):
    k+=1
    c=0
    for d in range(2,int(i**0.5)):
        if i%d==0:
            c+=2
            if c>0:
                break
    if c==0:
        print(k,i)