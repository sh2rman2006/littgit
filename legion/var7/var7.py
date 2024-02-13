"""2"""
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((x==y)or (y and z) or w)==0:
#                     print(x,y,z,w)

# x y w z
"""5"""
# for n in range(1,10000):
#     r=bin(n)[2:]
#     if n%2==0:
#         r+='00'
#     else:
#         r+='11'
#     if int(r,2)<102:
#         print(n)
"""7"""
# i=8
# 297
"""8"""
# from itertools import *
# count=0
# a=permutations('0123456789',r=6)
# b=[list(i) for i in a]
# for i in b:
#     if ''.join(i)[-2:]=="26" and i[0]!='0':
#         j=0
#         for k in i:
#             if k in '02468':
#                 j+=1
#         if j==4 or j==3:
#             count+=1
# print(count)
"""9"""
# for i in open('9_legvar7.csv'):
#     a=i.split(';')
#     print(a)
#
#
#
"""11"""
# i=5
"""12"""
# sm=0
# a='>'+'1'*15+'4'*16+'6' *20
# while( '>1' in a) or ('>4' in a ) or ('>6' in a):
#     if '>1' in a :
#         a=a.replace('>1','4161>',1)
#     if '>4' in a :
#         a=a.replace('>4','1611>',1)
#     if '>6' in a :
#         a=a.replace('>6','414>',1)
# for i in a  :
#     if i!=">":sm+=int(i)
#
# print(sm)
"""13"""
"""14"""
# a=125**300*5**300-25**70-100
# def perevod(n,s):
#     string=''
#     while n>0:
#         string+=str(n%s)
#         n//=s
#     return string[::-1]
# print(perevod(a,5).count("4"))
"""15"""
# for a in range(1,601):
#     if not((120%a==0)<=(not(168%a==0))):
#         print(a)
"""16"""
# def f(n):
#     if n==1:
#         return 3
#     if n%2==0:
#         return n+f(n//2)
#     if n>1 and n%2!=0:
#         return 3*f(n-1)
# print(f(115))
"""17"""
# a=open("17_legvar7.txt")
# count=0
# mx=1
# for i in a :
#     if i.count('6')>0:
#         mx=min(mx,int(i))
#         count+=1
# print(count,mx)
"""18"""
"""19"""
# def f(n,k,k1):
#     if n==3 and k+k1>76:
#         return 1
#     if n==3 and k+k1<77:
#         return 0
#     if n<3 and k+k1>76:
#         return 0
#     if n%2==0:
#         return f(n+1,k+1,k1) or f(n+1,k,k1+1) or f(n+1,k+k1*2,k1) or f(n+1,k,k1+2*k)
#     else:
#         return f(n+1,k+1,k1) or f(n+1,k,k1+1) or f(n+1,k+k1*2,k1) or f(n+1,k,k1+2*k)
# for i in range(1,68):
#     if f(1,9,i):
#         print(i)
"""20"""
# def f(n,k,k1):
#     if n==4 and k+k1>76:
#         return 1
#     if n==4 and k+k1<77:
#         return 0
#     if n<4 and k+k1>76:
#         return 0
#     if n%2!=0:
#         return f(n+1,k+1,k1) or f(n+1,k,k1+1) or f(n+1,k+k1*2,k1) or f(n+1,k,k1+2*k)
#     else:
#         return f(n+1,k+1,k1) and f(n+1,k,k1+1) and f(n+1,k+k1*2,k1) and f(n+1,k,k1+2*k)
# for i in range(1,68):
#     if f(1,9,i):
#         print(i)
"""21"""
# def f(n,k,k1):
#     if (n==3 or n==5 )and k+k1>76:
#         return 1
#     if n==5 and k+k1<77:
#         return 0
#     if n<5 and k+k1>76:
#         return 0
#     if n%2==0:
#         return f(n+1,k+1,k1) or f(n+1,k,k1+1) or f(n+1,k+k1*2,k1) or f(n+1,k,k1+2*k)
#     else:
#         return f(n+1,k+1,k1) and f(n+1,k,k1+1) and f(n+1,k+k1*2,k1) and f(n+1,k,k1+2*k)
# a=set()
# for i in range(1,68):
#     if f(1,9,i):
#         print(i)
#         a.add(i)
#
# print('/////')
# def f1(n,k,k1):
#     if n==3 and k+k1>76:
#         return 1
#     if n==3 and k+k1<77:
#         return 0
#     if n<3 and k+k1>76:
#         return 0
#     if n%2==0:
#         return f1(n+1,k+1,k1) or f1(n+1,k,k1+1) or f1(n+1,k+k1*2,k1) or f1(n+1,k,k1+2*k)
#     else:
#         return f1(n+1,k+1,k1) and f1(n+1,k,k1+1) and f1(n+1,k+k1*2,k1) and f1(n+1,k,k1+2*k)
# b=set()
# for i in range(1,68):
#     if f1(1,9,i):
#         print(i)
#         b.add(i)
# print(a-b)
"""23"""
# def f(n,s):
#     if n==s:
#         return 1
#     if n>s:
#         return 0
#     return f(n+1,s) +f(n*2,s)
# print(f(2,10)*f(10,32))
"""24"""
# a=open('24.txt').readline()
# b=a.split(" ")
# mx=0
# for i in b:
#     mx=max(len(i),mx)
# print(mx)
"""25"""
# for i in range(153222,153270+1):
#     for d in range(1,int(i**0.5)):
#         a=(i-d**2)**0.5
#         if a%1==0:
#             print(d,a,'//',i)


