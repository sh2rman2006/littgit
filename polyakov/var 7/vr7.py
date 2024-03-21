"""2"""
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((x and (not y))or (x==z) or w)==0:
#                     print(x,y,z,w)
# 1z 2y 3w 4x
"""5"""
# for n in range(1,10001):
#     r=bin(n)[2:]
#     if r.count('1')>r.count('0'):
#         r+='0'
#     else:
#         r+='11'
#     if int(r,2)>2019:
#         print(n);break
"""8"""
# from itertools import *
# a=[list(i) for i in product('ёиклнос',repeat=5)]
# for i in range(len(a)):
#     if a[i].count('ё')>=2 and a[i][0]!='о' and a[i][1]=='к':
#         print(i+1)
"""9"""
# count=0
# for i in open('9vr7.csv'):
#     a=list(map(int,i.split(';')))
#     nm=[i for i in a if i!=max(a)]
#     for k in range(a.count(max(a))-1):
#         nm.append(max(a))
#     b=sorted(a.copy())
#     pr=[b[-1]+b[0],b[1]+b[2]]
#     if max(a)<sum(nm) and pr[0]==pr[1]:
#         count+=1
# print(count)
"""12"""
# for n in range(4,10000):
#     a='5'+'2'*n
#     while '72' in a or '522' in a or '2222' in a :
#         if '72' in a:
#             a=a.replace('72','2',1)
#         if '522' in a:
#             a=a.replace('522','27',1)
#         if '2222' in a:
#             a=a.replace('2222','5',1)
#     if sum(map(int,a))==63:
#         print(n);break
"""13"""
# from ipaddress import *
# count=0
# net=ip_network('184.178.54.144/255.255.255.240',False)
# for i in net :
#     ln=bin(int(i))[2:]
#     if ln.count('111')>0:
#         count+=1
# print(count)
"""16"""
# from sys import *
# setrecursionlimit(10000)
# def f(n):
#     if n>=3210:
#         return 1
#     else:
#         return f(n+3)+7
# def g(n):
#     if n<10:
#         return n
#     else:
#         return g(n-3)+5
# print(f(15)-g(3000))
"""17"""
# a=[int(i) for i in open('17-379.txt')]
# count=0
# mx=0
# m=max([int(i) for i in a if str(i)[-2:]=='15'])
# for i in range(len(a)-2) :
#     k=0
#     if len(str(a[i]))==4:
#         k+=1
#     if len(str(a[i+1]))==4:
#         k+=1
#     if len(str(a[i+2]))==4:
#         k+=1
#     if k==1 and (a[i]+a[i+1]+a[i+2])>=m:
#         count+=1
#         mx=max(mx,a[i]+a[i+1]+a[i+2])
# print(count,mx)
"""23"""
# def f(n,s):
#     if n==s:
#         return 1
#     if n<s:
#         return 0
#     return f(n-3,s)+f(n//2,s)
# print(f(108,42)*f(42,12))
"""24"""
# a=open('24-208.txt').readline().replace('2022','*')
# mx=0
# for i in range(len(a)):
#     count=0
#     if a[i]=='*':
#         cz=0
#         for k in range(i+1,len(a)):
#             if cz==5:
#                 mx=max(mx,count)
#                 break
#             if a[k]=='*':
#                 cz+=1
#                 count+=4
#             else:
#                 count+=1
# print(mx)













