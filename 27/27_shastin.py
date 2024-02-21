file=[int(i) for i in open('27A_shast.txt')]
sm=0
print(file,len(file))
for i in range(len(file)):
    if str(file[i])=='1':
        c1=0
        for k in range(i+1,len(file)):
            if str(file[k])=='0':
                c1+=1
                break
            else:
                c1+=1
        c2 = 0
        for k in range(i-1,-1,-1):
            if str(file[k])=='0':
                c2+=1
                break
            else:
                c2+=1
        if c1==0:
            sm+=c2
            print(i)
        if c2==0:
            sm+=c1
            print(i)
        if c1>0 and c2>0:
            sm+=min(c1,c2)
print(sm,'sm')