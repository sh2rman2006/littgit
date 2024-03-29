"""5"""
# def perevod(n,s):
#     string=''
#     while n>0:
#         string+=str(n%s)
#         n//=s
#     return string[::-1]
#
# for n in range(11,1001):
#     r=perevod(n,3)
#     if sum(map(int,r))%3==0:
#         r='20'+r
#     else:
#         r='10'+r
#     if int(r,3)<100:
#         print(n)
"""15"""
# for x in [k*0.25 for k in range(-10000,10000)]:
#     a=0
#     b=70<=x<=80
#     f= x%12==0 and b and x%a!=0
#     if f!=1:
#         print(x)
"""16"""
# from sys import *
# setrecursionlimit(10000)
#
# def f(n):
#     if n<=2:
#         return 5
#     else:
#         return a[n-2]+n
# a=[0]*(23023+2)
# for i in range(len(a)):
#     a[i]=f(i)
# print(f(23023))
"""13"""
from ipaddress import *



"""14"""
# def f(n,s):
#     for i in range(len(n)):
#         n[i]=n[i]*s**(len(n)-1-i)
#     return sum(n)
#
# for x in range(17):
#     a=f([1,2,3,4,6,x,1,7],17)+f([7,x,1,7,1],17)
#     if a%16==0:
#         print(a//16);break
"""17"""
# a=[int(i) for i in open('17-370 (1).txt')]
# s=max([i for i in a if len(str(abs(i)))==3 and str(sum(map(int,str(abs(i)))))[-1]=='3'])
# count=0
# mx=0
# for i in range(len(a)-1):
#     if (len(str(abs(a[i])))==4 and len(str(abs(a[i+1])))!=4) or (len(str(abs(a[i+1])))==4 and len(str(abs(a[i])))!=4):
#         if (a[i]**2+a[i+1]**2)%s==0:
#             count+=1
#             mx=max(mx,a[i]**2+a[i+1]**2)
# print(count,mx)
"""19"""
# def f(n,k):
#     if n==3 and k>72:
#         return 1
#     if n==3 and k<=72:
#         return 0
#     if n!=3 and k>72:
#         return 0
#     if n%2==0:
#         return f(n+1,k+1) or f(n+1,k+3) or f(n+1,k*2)
#     else:
#         return f(n+1,k+1) and f(n+1,k+3) and f(n+1,k*2)
#
# for s in range(1,73):
#     if f(1,s):
#         print(s)
"""20"""
# def f(n,k):
#     if n==4 and k>72:
#         return 1
#     if n==4 and k<=72:
#         return 0
#     if n!=4 and k>72:
#         return 0
#     if n%2!=0:
#         return f(n+1,k+1) or f(n+1,k+3) or f(n+1,k*2)
#     else:
#         return f(n+1,k+1) and f(n+1,k+3) and f(n+1,k*2)
#
# for s in range(1,73):
#     if f(1,s):
#         print(s)
"""21"""
# def f(n,k):
#     if (n==3 or n==5 )and k>72:
#         return 1
#     if n==5 and k<=72:
#         return 0
#     if n!=5 and k>72:
#         return 0
#     if n%2==0:
#         return f(n+1,k+1) or f(n+1,k+3) or f(n+1,k*2)
#     else:
#         return f(n+1,k+1) and f(n+1,k+3) and f(n+1,k*2)
#
# for s in range(1,73):
#     if f(1,s):
#         print(s)
#
# print('////')
#
# def f(n,k):
#     if n==3 and k>72:
#         return 1
#     if n==3 and k<=72:
#         return 0
#     if n!=3 and k>72:
#         return 0
#     if n%2==0:
#         return f(n+1,k+1) or f(n+1,k+3) or f(n+1,k*2)
#     else:
#         return f(n+1,k+1) and f(n+1,k+3) and f(n+1,k*2)
#
# for s in range(1,73):
#     if f(1,s):
#         print(s)
"""23"""
# def f(n,s):
#     if n==s:
#         return 1
#     if n>s:
#         return 0
#     return f(n+2,s)+f(n+4,s)+f(n+5,s)
# for s in range(32,1001):
#     if f(31,s)==1001:
#         print(s)
"""24"""
# a=open('24-191.txt').readline()
# count=0
# for i in range(len(a)):
#     if a[i]=='A':
#         r='A'
#         for k in range(i+1,i+15):
#             if k==len(a):
#                 break
#             if a[k]=="A":
#                 r+=a[k]
#                 break
#             if a[k]=='B':
#                 r+=a[k]
#                 break
#             r+=a[k]
#         if r.count("F")>0 and r[-1]=='B':
#             count+=1
# print(count)












