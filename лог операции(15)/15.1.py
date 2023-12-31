P=[str(i) for i in range(56,80)]
Q=[str(i) for i in range(63,86)]

for a in range(1,300):
    A=[str(i) for i in range(1,a+1)]
    count=0
    for x in range(1,300):
        if not((str(x) in P)<=(str(x)in Q)) <=(not(str(x)in Q)<=(str(x in A))) :
            count+=1
        if count==299:
            print(a)

