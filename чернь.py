"""5"""
# def perevod(n,s):
#     string=''
#     while n>0:
#         string+=str(n%s)
#         n//=s
#     return string[::-1]
#
#
# sum=0
# for n in range(10,100):
#     r=n
#     if perevod(n,7)[-1]=='6':
#         if n%2==0:
#             sm=0
#             for i in str(n):
#                 sm+=int(i)
#             r-=sm
#         else:
#             r-=1
#         if r%2!=0:
#             sum+=n
# print(sum)
"""8"""
from itertools import *
count=0
b=[list(i) for i in product('АЯНОКОДЖИ',repeat=6)]
for i in b:
    if i.count('А')==1 and i.count('О')==2 and i.count('И')==1 and i.count('Я')==1:
        print(i)
        sm=[]
        for k in i:
            if k=='А':sm.append(1)
            if k=='Я':sm.append(2)
            if k=='Н':sm.append(3)
            if k=='О':sm.append(4)
            if k=='К':sm.append(5)
            if k=='Д':sm.append(7)
            if k=='Ж':sm.append(8)
            if k=='И':sm.append(9)
        sm=sum(sm)
        if sm==15:
            count+=1
print(count)

