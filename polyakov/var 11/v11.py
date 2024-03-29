"""2"""
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (((x or y)==(y<=z))or w)==0:
#                     print(x,y,z,w)
# 1x 2z 3w 4y
"""5"""
# sm=0
# for n in range(10000,100000):
#     r=list(oct(n)[2:])
#     for i in range(len(r)):
#         if r[i] in '13579':
#             r[i]='2'
#     r=''.join(r)+str(n%8)
#     r=int(r,8)
#     if r%2023:
#         sm+=n
# print(sm)
"""8"""
# from itertools import *
# print(len([list(i) for i in product('приказ',repeat=4) if i.count('к')==1]))
"""9"""
# count=0
# for i in open('9-218.csv'):
#     a=list(map(int,i.split(';')))
#     if ((max(a)!=a[-1] and min(a)!=a[-1]) and (max(a)!=a[0] and min(a)!=a[0])):
#         a.sort()
#         if (a[2]-a[1])!=0:
#             if (a[-1]-a[0])%(a[2]-a[1])==0:
#                 count+=1
# print(count)
"""13"""
# from ipaddress import *
# count=0
# net=ip_network('158.132.161.128/255.255.255.128',False)
# for i in net:
#     ln=bin(int(i))[2:]
#     if ln[-1]=='1':
#         count+=1
# print(count)
"""15"""
# for a in range(1,2000):
#     flag=True
#     for x in range(1,900):
#         if (((x%2==0)<=(x%13!=0)) or (x+a>=1000))==0:
#             flag=False
#     if flag:
#         print(a)
#         break
"""16"""
# from sys import *
# setrecursionlimit(10000)
# def f(n):
#     if n>=2020:
#         return n
#     else:
#         return n+2+f(n+3)
# print(f(2012)-f(2023))
"""17"""
# a=[int(i) for i in open('17-375.txt')]
# m=min([i for i in a if len(str(i))==3 and len(set(str(i)))==3])
# count=0
# mn=1000000
# k=0
# for i in range(2500):
#     k-=1
#     if (a[i]*a[k])%m==0:
#         count+=1
#         mn=min(mn,a[i]+a[k])
# print(mn,count)
"""24"""
# a=open('24-197.txt').readline()
# a=a[::-1]
# a=a.replace('XYX','1').replace('XZX','1').replace('XXX','1')
# a=a.replace('YXY','1').replace('YZY','1').replace('YYY','1')
# a=a[::-1]
# count=1
# mx=0
# for i in range(len(a)-1):
#     if a[i]=='1' and a[i+1]=='1':
#         count+=1
#     else:
#         mx=max(mx,count)
#         count=1
# print(mx)
"""23"""
# def f(n,s,k):
#     if n==s:
#         return 1
#     if n>s or n==25 or n==30 or k==2:
#         return 0
#     return f(n+1,s,0)+f(n+2,s,0)+f(n*3,s,k+1)
# print(f(1,15,0)*f(15,43,0))
"""7"""
"""11"""
