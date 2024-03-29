"""5"""
# from itertools import *
# count=0
# for n in range(800,901):
#     a=[''.join(i) for i in permutations(str(n),r=2)]
#     b=[int(i) for i in a if i[0]!='0']
#     b=[min(b),max(b)]
#     if (b[1]-b[0])==30:
#         count+=1
# print(count)
"""8"""
# from itertools import *
# print(len([''.join(i) for i in permutations('шанель',r=len('шанель')) if i[0]!='ь' and ''.join(i).count('еаь')==0]))
"""9"""
# for i in open('var21.csv'):
#     i.replace(',','.')
#     a=list(map(float,i.split(';')))
#     print(a)
"""13"""
# from ipaddress import *
# net=ip_network('204.252.0.0/255.255.0.0',False)
# mx=0
# for i in net:
#     ln=bin(int(i))[2:]
#     mx=max(mx,ln.count('1'))
# print(mx)
"""14"""
# def a[n,s):
#     for i in range(len(n)):
#         n[i]=n[i]*s**(len(n)-1-i)
#     return sum(n)
# for x in range(23):
#     a=a[[7,x,3,8,5,9,6],23)+a[[1,4,x,3,6],23)+a[[6,1,x,7],23)
#     if a%22==0:
#         print(a//22);break
"""15"""
# for a in range(1,301):
#     flag=True
#     for x in range(1,301):
#         for y in range(1,301):
#             if (  ((x**2-3*x+2)>0)or (y>(x**2 +7)) or ((x*y)<a)  )==0:
#                 flag=False
#     if flag:
#         print(a)
"""16"""
# from sys import *
# setrecursionlimit(10000)
# def f(n):
#     if n<3:
#         return 1
#     else:
#         return a[n-1]+a[n-2]
#
# a=[0]*1010
# for i in range(len(a)):
#     a[i]=f(i)
# print((a[1006]-a[1004])/a[1005])
"""17"""
# a=[int(i) for i in open('17-1.txt')]
# sr=sum(a)/len(a)
# count=0
# mx=0
# for i in range(len(a)-2):
#     if (a[i]<sr or a[i+1]<sr or a[i+2]<sr) and (str(a[i])[-1]=='6' or str(a[i+1])[-1]=='6' or str(a[i+2])[-1]=='6'):
#         count+=1
#         mx=max(mx,a[i]+a[i+1]+a[i+2])
# print(count,mx)
"""23"""
# def f(n,s):
#     if n==s:
#         return 1
#     if n>s or n==25:
#         return 0
#     return f(n+1,s)+f(2*n+1,s)
# print(f(1,31))
"""24"""
# a=open('24-186.txt').readline()
# count=0
# for i in range(len(a)):
#     if a[i]=='7':
#         b=['7']
#         for k in range(i+1,len(a)):
#             if len(b)==11:
#                 break
#             if a[k] in '0123456789':
#                 b.append(a[k])
#         if len(b)==11 and ((int(b[0])+int(b[1]))==(int(b[-1])+int(b[-2]))):
#             count+=1
# print(count)
"""25"""
# for n in range(500000000,450000000,-1):
#     d=[]
#     for k in range(2,int(n**1/2)):
#         if n%k==0:
#             d.append(k)
#             d.append(n//k)
#     if (n**1/2)%1==0:
#         d.append(int(n**1/2))
#
#     if len(d)>5:
#         print(sorted(d)[5],len(d))










