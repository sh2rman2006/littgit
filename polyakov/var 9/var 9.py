"""2"""
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((x and y) or (y==z) or w)==0:
#                     print(x,y,z,w)
# 1z 2y 3w 4x
"""5"""
# for n in range(100,1000):
#     s=int(str(n)[0])*int(str(n)[1])
#     s1=int(str(n)[1])*int(str(n)[2])
#     a=''.join(map(str,sorted([s,s1])[::-1]))
#     if a=='240':
#         print(n)
"""8"""
# from itertools import *
# print(len([list(i) for i in product('вася',repeat=5) if i.count('а')>0]))
"""9"""
# count=0
# for i in open('9var9.csv'):
#     a=list(map(int,i.split(';')))
#     if (max(a) +min(a))%3==0 and ((sorted(a)[2]-sorted(a)[3])==(sorted(a)[0]-sorted(a)[1]) or (sorted(a)[1]-sorted(a)[3])==(sorted(a)[0]-sorted(a)[2])):
#         count+=1
# print(count)
"""13"""
# from ipaddress import *
# count=0
# net=ip_network('202.75.38.176/255.255.255.240',False)
# for i in net:
#     ln=bin(int(i))[2:]
#     if ln.count('111')==0 and ln.count('000')==0:
#         count+=1
# print(count)
"""14"""
# for x in range(12):
#     a=[5,x,9,x,4]
#     b=[7,x,x,6]
#     c=[5,5,x,x,8]
#     for i in range(len(a)):
#         a[i]=a[i]*12**(len(a)-1-i)
#     for i in range(len(b)):
#         b[i]=b[i]*14**(len(b)-1-i)
#     for i in range(len(c)):
#         c[i]=c[i]*16**(len(c)-1-i)
#     for y in range(19):
#         d=[3,y,x,7]
#         for i in range(len(d)):
#             d[i] = d[i] * 19 ** (len(d) - 1 - i)
#         otv= sum(a)+sum(b)+sum(c)+sum(d)
#         for d in range(2,int(otv**0.5)+1):
#             if otv%d==0:
#                 break
#         else:
#             print(x*y)
"""23"""
# def f(n,s):
#     if n==s:
#         return 1
#     if n<s:
#         return 0
#     return f(n-1,s)+f(n//2,s)
# print(f(30,12)*f(12,1))
"""17"""
# a=[int(i) for i in open('17-377.txt')]
# mx=0
# count=0
# f=max([i for i in a if i%17==0])
# for i in range(len(a)-1):
#     if (a[i]+a[i+1])>f:
#         count+=1
#         mx=max(mx,a[i]+a[i+1])
# print(mx,count)
"""16"""
# from sys import *
# setrecursionlimit(10000)
# def f(n):
#     if n>=10000:
#         return 1
#     if n<10000 and n%2==0:
#         return a[n+3]+7
#     if n<10000 and n%2==1:
#         return a[n+1]-3
# a=[0]*20001
# for i in range(len(a)):
#     a[i]=f(i)
# print(a[1]-a[2])
"""15"""
# for a in range(1,30001):
#     flag=True
#     for x in range(1,1001):
#         if ((x%10==0 and x%26==0 and (x>=300))<=(a<=x))==0:
#             flag=False
#     if flag:
#         print(a)
"""24"""
# a=open('24-1 (1).txt').readline()
# mx=0
# for i in range(len(a)):
#     if a[i]=='A':
#         ca=0
#         count=0
#         for k in range(i+1,len(a)):
#             if ca==6:
#                 mx=max(mx,count-1)
#                 break
#             if a[k]=='A':
#                 ca+=1
#                 count+=1
#             else:
#                 count+=1
# print(mx)

































