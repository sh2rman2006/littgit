"""2"""
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for w in range(2):
#             for z in range(2):
#                 if ((x and (not z)) or (y==z) or (not w))==0:
#                     print(x,y,z,w)
# 1w 2y 3z 4x
"""5"""
# for n in range(1,1001):
#     r=bin(n)[2:]
#     if n%2==0:
#         r+='01'
#     else:
#         r='1'+r+'1'
#     if int(r,2)>156:
#         print(n)
#         break
"""6"""
# from turtle import *
# left(90)
# s=Screen()
# s.screensize(1000,1000)
# tracer(0)
# ms=25
# pd()
# for i in range(2):
#     forward(13*ms)
#     right(90)
#     forward(18*ms)
#     right(90)
# pu()
# forward(5*ms)
# right(90)
# forward(9*ms)
# left(90)
# pd()
# for i in range(2):
#     forward(11*ms)
#     right(90)
#     forward(7*ms)
#     right(90)
#
#
# pu()
# for x in range(-25,25):
#     for y in range(-25,25):
#         goto(x*ms,y*ms)
#         dot(5)
#
# done()
"""7"""
"""8"""
# from itertools import *
# a=[list(i) for i in product('апрсу',repeat=5)]
#
# for i in range(len(a)):
#     if a[i].count('у')<2:
#         for k in range(len(a[i])-1):
#             if a[i][k]=='а' and a[i][k+1]=='а':
#                 break
#         else:
#             print(i)
#             break
"""9"""
# count=0
# for i in open('9_dosrok.csv'):
#     a=list(map(int,i.split(';')))
#     nm=[i for i in a if i!=max(a)]
#     for k in range(a.count(max(a))-1):
#         nm.append(max(a))
#     a.sort()
#     if max(a)<sum(nm) and ((a[-1]+a[0])==(a[1]+a[2]) or ((a[0]+a[2])==(a[1]+a[-1]))):
#         count+=1
# print(count)
"""12"""
# a='8'*45
# while ('1111' in a) or ('8888' in a):
#     if '1111' in a :
#         a=a.replace('1111','88',1)
#     if '8888' in a:
#         a = a.replace('8888', '11', 1)
# print(a)
"""13"""
# from ipaddress import *
# count=0
# net =ip_network('105.224.200.224/255.255.255.224',False)
# for i in net:
#     ln=bin(int(i))[2:]
#     if ln.count('1')%4==0:
#         count+=1
# print(count)
"""14"""
# def f(n,s):
#     for i in range(len(n)):
#         n[i]=n[i]*s**(len(n)-1-i)
#     return sum(n)
#
# for x in range(27):
#     a=f([1,2,3,x,2,4],27)+f([1,3,5,x,7,8],27)
#     if a%26==0:
#         print(a//26)
"""15"""
# for a in range(1,501):
#     flag=True
#     for x in range(1,501):
#         if ((x%a!=0)<=((x%28==0)<=(x%49!=0)))==0:
#             flag=False
#     if flag:
#         print(a)
"""16"""
# from sys import *
# setrecursionlimit(10000)
# def f(n):
#     if n<=7:
#         return 1
#     else:
#         return n+2+f(n-1)
# print(f(2024)-f(2020))
"""17"""
# a=[int(i) for i in open('17_15333.txt')]
# c=max([i for i in a if i%19==0])
# count=0
# mx=0
# for i in range(len(a)-1):
#     if a[i]>c or a[i+1]>c:
#         count+=1
#         mx=max(mx,a[i]+a[i+1])
# print(count,mx)
"""18"""
"""19"""
# def f(n,k,k1):
#     if n==3 and (k+k1)>122:
#         return 1
#     if n!=3 and (k+k1)>122:
#         return 0
#     if n==3 and (k+k1)<123:
#         return 0
#     if n%2==0:
#         return f(n+1,k+1,k1) or f(n+1,k,k1+1) or f(n+1,k*2,k1) or f(n+1,k,k1*2)
#     else:
#         return f(n + 1, k + 1, k1) or f(n + 1, k, k1 + 1) or f(n + 1, k * 2, k1) or f(n + 1, k, k1 * 2)
#
# for s in range(1,110):
#     if f(1,13,s):
#         print(s)
"""20"""
# def f(n,k,k1):
#     if n==4 and (k+k1)>122:
#         return 1
#     if n!=4 and (k+k1)>122:
#         return 0
#     if n==4 and (k+k1)<123:
#         return 0
#     if n%2!=0:
#         return f(n+1,k+1,k1) or f(n+1,k,k1+1) or f(n+1,k*2,k1) or f(n+1,k,k1*2)
#     else:
#         return f(n + 1, k + 1, k1) and f(n + 1, k, k1 + 1) and f(n + 1, k * 2, k1) and f(n + 1, k, k1 * 2)
#
# for s in range(1,110):
#     if f(1,13,s):
#         print(s)
"""21"""
# def f(n,k,k1):
#     if (n==5 or n==3) and (k+k1)>122:
#         return 1
#     if n!=5 and (k+k1)>122:
#         return 0
#     if n==5 and (k+k1)<123:
#         return 0
#     if n%2==0:
#         return f(n+1,k+1,k1) or f(n+1,k,k1+1) or f(n+1,k*2,k1) or f(n+1,k,k1*2)
#     else:
#         return f(n + 1, k + 1, k1) and f(n + 1, k, k1 + 1) and f(n + 1, k * 2, k1) and f(n + 1, k, k1 * 2)
#
# a=set()
# for s in range(1,110):
#     if f(1,13,s):
#         a.add(s)
#         print(s)
# print('///////')
#
# def f(n,k,k1):
#     if n==3 and (k+k1)>122:
#         return 1
#     if n!=3 and (k+k1)>122:
#         return 0
#     if n==3 and (k+k1)<123:
#         return 0
#     if n%2==0:
#         return f(n+1,k+1,k1) or f(n+1,k,k1+1) or f(n+1,k*2,k1) or f(n+1,k,k1*2)
#     else:
#         return f(n + 1, k + 1, k1) and f(n + 1, k, k1 + 1) and f(n + 1, k * 2, k1) and f(n + 1, k, k1 * 2)
#
# b=set()
# for s in range(1,110):
#     if f(1,13,s):
#         b.add(s)
#         print(s)
# print(a-b)
"""23"""
# def f(n,s):
#     if n==s:
#         return 1
#     if n>s:
#         return 0
#     return f(n+1,s)+f(n*2,s)
# print(f(4,8)*f(8,10)*f(10,15))
"""24"""
# file=open('24_15339.txt').readline()
# bukv='ABC'
# ch='6789'
# count=1
# mx=0
# for i in range(len(file)-1):
#     if ((file[i] in bukv) and (file[i+1] in bukv)) or ((file[i] in ch) and (file[i+1] in ch)):
#         mx=max(mx,count)
#         count=1
#     else:
#         count+=1
# print(mx)
"""25"""
# from fnmatch import *
# for i in range(2024,10**10+1,2024):
#     if fnmatch(str(i),'1*2322?2'):
#         print(i,i//2024)
"""26"""
# file=[int(i) for i in open('26_15341.txt')]
# file.sort(reverse=1)
# count=0
# s=[file[0]]
# for i in range(len(file)):
#     if (s[-1]-file[i])>=8:
#         s.append(file[i])
#         count+=1
# print(count,s[-1])




