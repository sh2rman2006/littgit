"""2"""
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if  ((w or x or y) <= (((y or z) and x) or (y and (w or z))))==0:
#                     print(x,y,z,w)
# y1
# 3z
# 2w
# 4x
"""5"""
# count=0
# for n in range(100000000,1000000000):
#     sm=sum(list(map(int,str(n))))
#     r=bin(sm)[2:]
#     if r.count('1')%2==0:
#         r='1'+r+'00'
#     else:
#         r='10'+r+'1'
#     if int(r,2)==21:
#         count+=1
#         print(n)
# print(count)
"""7"""
"""8"""
# from itertools import *
# a=[list(i) for i in product('аимря',repeat=4)]
# count=0
# for i in a:
#     count+=1
#     if count==211:
#         print(i)
"""9"""
# count=0
# for i in open('9_var1pol.csv'):
#     a=list(map(int,i.split(';')))
#     rp=[i for i in a if a.count(i)==2]
#     b=sorted(a)
#     if len(rp)==2 and ((b[-1]+b[-2])/(b[0]+b[1]))>2 and b[-1]%b[0]!=0:
#         count+=1
# print(count)
"""11"""
"""12"""
# mx=0
# for n in range(4,1000):
#     a='1'+'2'*n
#     while '12' in a or '322' in a or '222' in a:
#         if '12' in a :
#             a=a.replace('12','2',1)
#         if '322' in a :
#             a=a.replace('322','21',1)
#         if '222' in a :
#             a=a.replace('222','3',1)
#     mx=max(mx,len(a))
# print(mx)
"""13"""
# count=0
# from ipaddress import *
# a=ip_network('117.32.0.0/255.224.0.0',False)
# for i in a:
#     b=str(i).split('.')
#     rp=[i for i in b if b.count(i)==2]
#     if len(rp)==2:
#         count+=1
# print(count)
"""14"""
# a=7*5**123 + 6*5**111 - 5*25**50 + 4*125**30 - 3*5**10
# def perevod(n,s):
#     string=''
#     while n>0:
#         string+=str(n%s)
#         n//=s
#     return string[::-1]
# a=perevod(a,5)
# print(a.count('4'))
"""16"""
# from sys import *
# setrecursionlimit(10000)
# def f(n):
#     if n==1:
#         return 1
#     if n>1:
#         return n+f(n-1)
# count=0
# for n in range(1,101):
#     if f(2023)//f(n)%2==0:count+=1
# print(count)
"""17"""
# a=[int(i) for i in open('17-385.txt')]
# mx=0
# for i in range(len(a)-1):
#     sm=sum(map(int,str(a[i])))
#     if sm==4:
#         mx=max(mx,a[i])
# ms=0
# count=0
# for i in range(len(a)-1):
#     if a[i]>mx and a[i+1]>mx:
#         count+=1
#         ms=max(ms,sum(map(int,str(a[i])+str(a[i+1]))))
# print(count,ms)
"""19"""
# def f(n,s):
#     if n==3 and s>36:
#         return 1
#     if n==3 and s<37:
#         return 0
#     if n<3 and s>36:
#         return 0
#     if n%2==0:
#         return f(n+1,s+1) or f(n+1,s+2) or f(n+1,s*3)
#     else:
#         return f(n+1,s+1) and  f(n+1,s+2) and  f(n+1,s*3)
# for s in range(1,37):
#     if f(1,s):
#         print(s)
"""20"""
# def f(n,s):
#     if n==4 and s>36:
#         return 1
#     if n==4 and s<37:
#         return 0
#     if n<4 and s>36:
#         return 0
#     if n%2!=0:
#         return f(n+1,s+1) or f(n+1,s+2) or f(n+1,s*3)
#     else:
#         return f(n+1,s+1) and  f(n+1,s+2) and  f(n+1,s*3)
#
#
# for s in range(1,37):
#     if f(1,s):
#         print(s)
"""21"""
# def f(n,s):
#     if (n==3 or n==5) and s>36:
#         return 1
#     if n==5 and s<37:
#         return 0
#     if n<5 and s>36:
#         return 0
#     if n%2==0:
#         return f(n+1,s+1) or f(n+1,s+2) or f(n+1,s*3)
#     else:
#         return f(n+1,s+1) and  f(n+1,s+2) and  f(n+1,s*3)
#
# for s in range(1,37):
#     if f(1,s):
#         print(s)
#
# print('///')
# def lp(n,s):
#     if n==3 and s>36:
#         return 1
#     if n==3 and s<37:
#         return 0
#     if n<3 and s>36:
#         return 0
#     if n%2==0:
#         return lp(n+1,s+1) or lp(n+1,s+2) or lp(n+1,s*3)
#     else:
#         return lp(n+1,s+1) and  lp(n+1,s+2) and  lp(n+1,s*3)
# for s in range(1,37):
#     if lp(1,s):
#         print(s)
"""23"""
# def f(n,s):
#     if n==s:
#         return 1
#     if n>s:
#         return 0
#     return f(n+1,s)+f(n+2,s)+f(n+5,s)
# print(f(21,30))
"""24"""
# ch='0123456789'
# a=open('24-264.txt').readline()
# mx=0
# count=1
# for i in range(len(a)-1):
#     if ((a[i] in ch) and (a[i+1] not in ch)) or((a[i] not in ch) and (a[i+1]  in ch))  :
#         count+=1
#     else:
#         mx=max(mx,count)
#         count=1
# print(mx)
"""25"""
# from fnmatch import *
# for n in range(2025,10**8+1,2025):
#     if fnmatch(str(n),'12*34?5'):
#         print(n,n//2025)
# print('')
