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


