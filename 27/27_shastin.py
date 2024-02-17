a=[str(i.replace("\n",'')) for i in open('27A_shastin.txt')]
a=''.join(a)
sm=0
for i in range(len(a)):
    if a[i]=='1':
        c1=0
        c2=0
        for k in range(i+1,len(a)):
            if a[k]=='0':
                c1+=1
                break
            else:
                c1+=1
        for l in range(i,0,-1):
            if a[l] == '0':
                c2 += 1
                break
            else:
                c2 += 1
        sm+=min(c1,c2)
print(sm)
