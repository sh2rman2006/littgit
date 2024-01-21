"""2"""
# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((x and (not y)) or (y==z) or (not w))==0:
#                     print(x,y,z,w)
# 1w 2z 3y 4x
"""5"""
# for n in range(1,1000):
#     r=bin(n)[2:]
#     if n%3==0:
#         r+=r[-3:]
#     else:
#         r+=bin(n%3*3)[2:]
#     if int(r,2)>151:
#         print(int(r,2))
"""6"""
# from turtle import *
# a=Screen()
# a.screensize(10000,10000)
# ms=25
# tracer(0)
# left(90)
# pd()
# for i in range(7):
#     forward(10*ms)
#     right(120)
# pu()
# for x in range(-10,51):
#     for y in range(-10,51):
#         goto(x*ms,y*ms)
#         dot(5)
# done()
"""8"""
# from itertools import *
# a=permutations("01234567",r=5)
# b=[list(i) for i in a]
# count=0
# for i in b:
#     if i[0]!="0" and  i.count("1")==0:
#         for ind in range(len(i)-1):
#             if (int(i[ind])%2==0 and int(i[ind+1])%2!=0) or (int(i[ind])%2!=0 and int(i[ind+1])%2==0):
#                 count+=1
# print(count)
"""12"""
# for n in range(3,10001):
#     a="5"+"2"*n
#     while ("52"in a) or ("2222"in a) or ("1122" in a):
#         if "52" in a:
#             a=a.replace("52","11",1)
#         if "2222" in a:
#             a=a.replace("2222","5",1)
#         if "1122" in a:
#             a=a.replace("1122","25",1)
#     suma=0
#     for i in a:
#         suma+=int(i)
#     if suma==64:
#         print(n)
"""14"""
# for x in range(19):
#     a=(9*19**7+8*19**6+8*19**5+9*19**4+7*19**3+x*19**2+2*19**1+1*19**0)+(2*19**4+x*19**3+9*19**2+2*19**1+3*19**0)
#     if a%18==0:
#         print(a/18)
"""15"""
# for a in range(1,301):
#     count=0
#     for x in range(1,301):
#         for y in range(1,301):
#             if (x+2*y<a)or (y>x)or (x>60):
#                 count+=1
#     if count==300**2:
#         print(a)
"""16"""
#

























