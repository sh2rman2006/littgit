file=[int(i) for i in open('27A_shastin.txt')]
sm=0
for i in range(len(file)):
    if str(file[i])=='1':
        c1=0
        print(i,'////')
        for k in range(i+1,len(file)):
            if file[k]=='0':
                c1+=1
                break
            else:
                c1+=1

        c2 = 0
        for k in range(i-1,-1,-1):
            if file[k]=='0':
                c2+=1
                break
            else:
                c2+=1
        sm+=min(c1,c2)
print(sm)