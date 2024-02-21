#10
from math import *
# sm=0
# for i in range(2,2000001):
#     count=0
#     for d in range(2,round(i**(1/2))+1):
#         if i**(1/2)%1==0:
#             count+=1
#         elif i%d==0:
#             count+=2
#     if count==0:
#         sm+=i
# print(sm)
#готово

"""10"""
# sm=0
# for i in range(2,2000000):
#     count=0
#     for d in range(2,int(i**0.5)+1):
#         if i%d==0:
#             count+=1
#             if count>0:
#                 break
#     else:
#         sm+=i
# print(sm)
"""16"""
# sm=0
# a=str(2**1000)
# for i in a:
#     sm+=int(i)
# print(sm)
"""20"""
# sm=0
# for i in range(1,101):
#     sm+=i
# print(sm)
"""21"""
# def f(n):
#     sm=1
#     for d in range(2,int(n**0.5)):
#         if n%d==0:
#             sm=sm+d+n//d
#     if n**0.5%1==0:
#         sm+=int(n**0.5)
#     return sm
# sm=0
# for i in range(10000):
#     for j in range(i+1,10000):
#         if f(i)==j and f(j)==i:
#             print(i,j,"наши числа")
#             sm=sm+i+j
#             break
# print(sm)
"""24"""
# from itertools import *
# a=permutations("0123456789",r=10)
# b=[list(i) for i in a]
# print(b[999999])
"""25"""
# s=[1,1]
# def fib(a):
#     f=s[-1]+s[-2]
#     s.append(f)
#     if len(s)==a:
#         return s
#     else:
#         return fib(a)
# print(fib(12))
# работает без перебора и не на больших числах
"""29"""
# a=[i**d for i in range(2,101) for d in range(2,101)]
# a.sort()
# b=set()
# for i in a:
#     b.add(i)
# print(len(b))
"""30"""
# maxsm=0
# for i in range(1,10000000):
#     sm=0
#     for j in str(i):
#         sm+=int(j)**5
#     if sm==i:
#         maxsm+=sm
#         print(i)
# print(maxsm,"///")
"""34"""
# from math import *
# i=3
# while True:
#     n=0
#     for s in str(i):
#         n+=factorial(int(s))
#     if n==i:
#         print(i)
#         i+=1
#     else:
#         i+=1
"""35"""
# countch=0
# from itertools import *
# for i in range(2,1000001):
#     count=0
#     for d in range(2,int(i**0.5)+1):
#         if i%d==0:
#             break
#     else:
#         b = [list(k) for k in permutations(str(i), len(str(i)))]
#         k=0
#         for ch in b:
#             if ch[0]=='0':
#                 while ch[0]=='0':
#                     ch=ch[1:]
#             ch=int(''.join(ch))
#             for dch in range(2,int(ch**0.5)+1):
#                  if ch%dch==0:
#                     k+=1
#                     break
#         if k==0:
#             countch+=1
# print(countch)
"""46"""
# prst=[]
# for i in range(2,10001):
#     for d in range(2,int(i**0.5)+1):
#         if i%d==0:
#             break
#     else:
#         prst.append(i)
# b=[]
# for i in range(3,10001,2):
#     count=0
#     ch=0
#     for k in range(3,10001,2):
#         c=i*k
#         ch=0
#         b.append(c)
#         d=[i for i in prst if i<c]
#         for l in d:
#             if ch>0:
#                 break
#             for j in range(1,26):
#                 if l+2*(j**2)==c:
#                     ch+=1
#     if ch==0:
#         print(b[-1])
#         break



















