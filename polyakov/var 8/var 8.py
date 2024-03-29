"""2"""
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (x or (not y))and (not(z==x)) and (not w):
#                     print(x,y,z,w)
# 1w 2y 3x 4z
"""5"""
# for n in range(1,1001):
#     r=bin(n)[2:]
#     if r.count('1')%2!=0:
#         r+='11'
#     else:
#         r='11'+r
#     if int(r,2)>102:
#         print(n);break
"""7"""
"""8"""
# from itertools import *
# a=[list(i) for i in product('ьзплеа',repeat=5)]
# a=a[:387]
# print(len([''.join(i) for i in a if i[-1]=='ь']))
"""9"""
# count=0
# for i in open('9-v8.csv'):
#     a=list(map(int,i.split(';')))
#     ch=[i for i in a if i%2==0]
#     n=[i for i in a if i%2==1]
#     if sum(n)>sum(ch):
#         count+=1
# print(count)
"""13"""
# from ipaddress import *
# net=ip_network('202.75.38.160/255.255.255.240',False)
# count=0
# for i in net:
#     ln=bin(int(i))[2:]
#     if ln.count('111')>0:
#         count+=1
# print(count)
"""15"""
# for a in range(1,501):
#     flag=True
#     for x in range(1,501):
#         if ((a+x<123)<=((x%5==0)<=(x%7!=0)))==0:
#             flag=False
#     if flag:
#         print(a);break
"""16"""
# from sys import *
# setrecursionlimit(10000)
# def f(n):
#     if n>=2025:
#         return n
#     else:
#         return a[n+1]-a[n+2]+7
# a=[0]*2030
# for i in range(2025,0,-1):
#     a[i]=f(i)
# print(a[15]-a[24])
"""17"""
# a=[int(i) for i in open('17-378.txt')]
# ms=max([abs(i) for i in a if i%1001==0])
# mn=10000000000
# count=0
# for i in range(len(a)-1):
#     if (len(str(abs(a[i])))==3 or len(str(abs(a[i+1])))==3) and (a[i]+a[i+1])>ms:
#          count+=1
#          mn=min(mn,a[i]+a[i+1])
# print(count,mn)
"""23"""
# def f(n,s):
#     if n==s:
#         return 1
#     if n<s:
#         return 0
#     return f(n-2,s)+f(n//2,s)
# print(f(28,10)*f(10,1))
"""24"""
# a=open('24-1.txt').readline()
# mx=0
# for i in range(len(a)):
#     if a[i]=='A' or a[i]=='B' or a[i]=='X':
#         count=0
#         v=0
#         for k in range(i+1,len(a)):
#             if v==6:
#                 count-=1
#                 break
#             if a[k] == 'A' or a[k] == 'B' or a[k] == 'X':
#                 v+=1
#                 count+=1
#             else:
#                 count+=1
#         mx=max(mx,count)
# print(mx)
"""11"""


