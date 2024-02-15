
from itertools import *
a1=[]
a2=[]
for n in range(100,1000):
    l=[''.join(i) for i in permutations(str(n),r=2)]
    count=0
    for k in l :
        while k[0]=='0' and len(k)>1:
            k=k[1:]
        for d in range(2,int(int(k)**0.5)+1):
            if int(k)%d==0:break
        else:count+=1
    if count==6:
        print(n)






