for B in range(1,401):
    count=0
    for x in range(1,401):
        if ((x&500!=0) and (x&200==0))<=(not(x&B==0)):
            count+=1
    if count==400:
        print(B)