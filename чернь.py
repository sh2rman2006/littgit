file=[int(i) for i in open('8 60 1 40.txt')]
sm=0
print(file,len(file))
for i in range(len(file)):
    if str(file[i])=='1':
        c1=0
        print(i,'i')
        for k in range(i+1,len(file)):
            if str(file[k])=='0':
                c1+=1
                break
            else:
                c1+=1
        print(c1,'c1')
        c2 = 0
        for k in range(i-1,-1,-1):
            if str(file[k])=='0':
                c2+=1
                break
            else:
                c2+=1
        print(c2,'c2')
        sm+=min(c1,c2)
print(sm,'sm')