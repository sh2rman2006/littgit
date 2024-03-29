"""5"""
# for n in range(1,1001):
#     r=bin(n)[2:]
#     if n%2==1:
#         r=r.replace('1','*')
#         r=r.replace('0','1')
#         r=r.replace('*','0')
#     r=r.replace('1','11')
#     r=r.replace('0','00')
#     if int(r,2)>60:
#         print(n);break
"""7"""
"""8"""
# from itertools import *
# a=[list(i) for i in product('0123456789abcde',repeat=5)]
# count=0
# for i in a :
#     if i[0]!='0':
#         f=0
#         for k in range(0,len(i),2):
#             if ((int(i[k],15)%3==0))==0:
#                 break
#         else:
#             f+=1
#         for k in range(1,len(i),2):
#             if (int(i[k],15)%2 ==0 )==0:
#                 break
#         else:
#             f+=1
#         if f==2:
#
#             count+=1
# print(count)
"""9"""
"""14"""
# def a[n,s):
#     for i in range(len(n)):
#         n[i]=n[i]*s**(len(n)-1-i)
#     return sum(n)
#
# for p in range(2,27):
#     for q in range(2, 27):
#         a=a[[2,4,3,5,1],p)
#         b=a[[1,4,3,2,5],q)
#         if a==b:
#             print(a)
"""16"""
from sys import *
setrecursionlimit(10000)
def f(n):
    if n>=10000:
        return n
    if n<10000 and n%4==0:
        return n/4+a[n//4+2]
    if n<10000 and n%4!=0:
        return 1+a[n+2]

a=[0]*10100
for i in range(len(a)-1,0,-1):
    a[i]=f(i)
    print(a[i])
print(a[174]-a[3])