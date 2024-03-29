"""2"""
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((x<=(y and w)) and (z<=(x or y)))!=w:
#                     print(x,y,z,w)
"""5"""
# def perevod(n,s):
#     string=[]
#     while n>0:
#         string.append(n%s)
#         n//=s
#     return string[::-1]
#
# def f(n,s):
#     k=[0]*len(n)
#     for i in range(len(n)):
#         k[i]=n[i]*s**(len(n)-1-i)
#     return sum(k)
#
# otv=[]
# for n in range(12,1001):
#     r=perevod(n,12)
#     if n%12==0:
#         r.append(r[-2])
#         r.append(r[-2])
#     else:
#         r.append(perevod(n%12*9,12)[0])
#     if f(r,12)>300:
#         otv.append(f(r,12))
# print(min(otv))
"""8"""
"""9"""
# count=0
# for i in open('9-v17.csv'):
#     a=list(map(int,i.split(';')))
#     rp=[i for i in a if a.count(i)==2]
#     if len(rp)==6 and (sorted(set(rp))[0]**2+sorted(set(rp))[1]**2)==sorted(set(rp))[2]**2:
#         count+=1
# print(count)
"""13"""
# '00111101'
# '00111011'
# print(int('11111000',2))
"""14"""
# def f(n,s):
#     for i in range(len(n)):
#         n[i]=n[i]*s**(len(n)-1-i)
#     return sum(n)
#
# for x in range(13):
#     a=f([5,3,7,x,6,2,3],13)-f([6,x,3,5,x,2],13)
#     if a%3==0:
#         print(a)
"""17"""
# a=[int(i) for i in open('17-354.txt')]
# n=[]
# for i in a:
#     if len(str(i))>1:
#         if str(i)[-1]==str(i)[-2]:
#             n.append(i)
# n=sum(n)/len(n)
# count=0
# mx=0
# for i in range(len(a)-1):
#     if len(str(a[i]))>1 and len(str(a[i+1]))>1:
#         if str(a[i])[-1]==str(a[i+1])[-2] or str(a[i+1])[-1]==str(a[i])[-2]:
#             if (a[i]%11==0 and a[i+1]%11!=0) or (a[i]%11!=0 and a[i+1]%11==0):
#                 if (a[i]**2+a[i+1]**2)>=n**2:
#                     count+=1
#                     mx=max(mx,a[i]**2+a[i+1]**2)
# print(count,mx)
"""23"""
# def f(n,s):
#     if n==s:
#         return 1
#     if n>s or n==13:
#         return 0
#     return f(n+1,s)+f(n*2,s)+f(n*3,s)
# print(f(3,8)*f(8,18))
"""16"""
# from sys import *
# setrecursionlimit(10000)
# def f(n):
#     if n==0:
#         return 0
#     else:
#         return f(n//10)+(n%10)


