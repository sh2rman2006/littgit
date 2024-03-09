"""5"""
# def perevod(n,s):
#     string=''
#     while n>0:
#         string+=str(n%s)
#         n//=s
#     return string[::-1]
#
# for n in range(1,1001):
#     r=perevod(n,3)
#     if n%3==0:
#         r='1'+r+'02'
#     else:
#         r+=perevod((n%3)*4,3)
#     if int(r,3)<199:
#         print(n)
"""8"""
# from itertools import *
# gl='уа'
# print([''.join(i) for i in product('адуч',repeat=5) if i[0] in gl].index('удача')+1)
"""9"""
# count=0
# for i in open('9polvar4.csv'):
#     a=list(map(int,i.split(';')))
#     c=set(a)
#     rp=set([i for i in a if a.count(i)==3])
#     if len(c)==5 and len(rp)==1:
#         rp=int(''.join(map(str,rp)))
#         if (sum(c)/len(c))<=rp:
#             count+=1
# print(count)
"""13"""
# from ipaddress import *
# a=[str(2**i-1) for i in range(1,9)]
# print(a)
# net=ip_network('139.75.100.0/255.255.252.0',False)
# count=0
# for i in net:
#     n=str(i).split('.')
#     if n[-1] in a:
#         count+=1
#         print(n)
# print(count)
"""14"""
# def perevod(n,s):
#     string=''
#     while n>0:
#         string+=str(n%s)
#         n//=s
#     return string[::-1]
# print(perevod(7*512**3200+6*256**3100-5*64**3000-4*8**2900-1542,64).count('0'))
"""17"""
# count=0
# mx=0
# a=[int(i) for i in open('17-382.txt')]
# b=min([i for i in a if str(i)[-2:]=='11' and len(str(i))==3])
# for i in range(len(a)-1):
#     if ((len(str(a[i]))==3 and len(str(a[i+1]))!=3) or (len(str(a[i]))!=3 and len(str(a[i+1]))==3)) and abs(a[i]-a[i+1])%b==0:
#         count+=1
#         mx=max(mx,a[i]+a[i+1])
# print(mx,count)
"""16"""
# from sys import *
# setrecursionlimit(10000)
# def f(n):
#     if n<11:
#         return n
#     else:
#         return n+f(n-1)
# print(f(2024)-f(2021))
"""23"""
# def f(n,s):
#     if n==s:
#         return 1
#     if n>s or n==23:
#         return 0
#     return f(n+2,s)+f(n*3,s)+f(n*5,s)
# print(f(1,13)*f(13,75))
"""24"""
# file=open('24-212.txt').readline()
# gl='BCD'
# sogl='AO'
# count=0
# mx=0
# for i in range(len(file)-1):
#     if ((file[i] in sogl) and (file[i+1] in gl)) or ((file[i] in gl) and (file[i+1] in sogl)):
#         count+=1
#     else:
#         mx=max(mx,count)
#         count=0
# print(mx//2)
"""25"""
#
"""19"""
# def f(n,k1,k2):
#     if n==3 and k1*k2>122:
#         return 1
#     if n==3 and k1*k2<123:
#         return 0
#     if n<3 and k1*k2>122:
#         return 0
#     if n%2==0:
#         return f(n+1,k1+2,k2) or f(n+1,k1*2,k2) or f(n+1,k1,k2+2) or f(n+1,k1,k2*2)
#     else:
#         return f(n + 1, k1 + 2, k2) or f(n + 1, k1 * 2, k2) or f(n + 1, k1, k2 + 2) or f(n + 1, k1, k2 * 2)
# for s in range(1,41):
#     if f(1,3,s):
#         print(s)
"""20"""
# def f(n,k1,k2):
#     if n==4 and k1*k2>122:
#         return 1
#     if n==4 and k1*k2<123:
#         return 0
#     if n<4 and k1*k2>122:
#         return 0
#     if n%2!=0:
#         return f(n+1,k1+2,k2) or f(n+1,k1*2,k2) or f(n+1,k1,k2+2) or f(n+1,k1,k2*2)
#     else:
#         return f(n + 1, k1 + 2, k2) and f(n + 1, k1 * 2, k2) and f(n + 1, k1, k2 + 2) and f(n + 1, k1, k2 * 2)
# for s in range(1,41):
#     if f(1,3,s):
#         print(s)
"""21"""
# def f(n,k1,k2):
#     if (n==3 or n==5) and k1*k2>122:
#         return 1
#     if n==5 and k1*k2<123:
#         return 0
#     if n<5 and k1*k2>122:
#         return 0
#     if n%2==0:
#         return f(n+1,k1+2,k2) or f(n+1,k1*2,k2) or f(n+1,k1,k2+2) or f(n+1,k1,k2*2)
#     else:
#         return f(n + 1, k1 + 2, k2) and  f(n + 1, k1 * 2, k2) and f(n + 1, k1, k2 + 2) and f(n + 1, k1, k2 * 2)
# for s in range(1,41):
#     if f(1,3,s):
#         print(s)
# print('////////')
# def f(n,k1,k2):
#     if n==3 and k1*k2>122:
#         return 1
#     if n==3 and k1*k2<123:
#         return 0
#     if n<3 and k1*k2>122:
#         return 0
#     if n%2==0:
#         return f(n+1,k1+2,k2) or f(n+1,k1*2,k2) or f(n+1,k1,k2+2) or f(n+1,k1,k2*2)
#     else:
#         return f(n + 1, k1 + 2, k2) and f(n + 1, k1 * 2, k2) and f(n + 1, k1, k2 + 2) and f(n + 1, k1, k2 * 2)
# for s in range(1,41):
#     if f(1,3,s):
#         print(s)
"""22"""
"""18"""
"""12"""
# for n in range(4,10000):
#     a='1'+'8'*n
#     while '18' in a or '388' in a or '888' in a:
#         if '18' in a:
#             a=a.replace('18','8',1)
#         if '388' in a:
#             a=a.replace('388','81',1)
#         if '888' in a:
#             a=a.replace('888','3',1)
#     if a.count('1')==3:
#         print(n)
#         break
"""7"""
"""11"""
"""4"""
"""2"""
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (x<=y) and ((not y)==z) and w:
#                     print(x,y,z,w)
# 1z 2w 3y 4x
"""3"""
"""1"""





