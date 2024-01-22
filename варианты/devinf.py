# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (w or y)and (x<=(not z))and (not w):
#                     print(x,y,z,w)
"""5"""
# for n in range(1,1000001):
#     r=bin(n)[2:]
#     r=r[::-1]
#     if r[0]=="0":
#         r="1"+r
#     r+=bin(n)[2:]
#     if int(r,2)<=6000:
#         print(n)
"""6"""
# from turtle import *
# a=Screen()
# a.screensize(10000,10000)
# ms=25
# tracer(0)
# left(90)
# pd()
# for i in range(2):
#     forward(4*ms)
#     right(90)
#     forward(32*ms)
#     right(90)
# pu()
# forward(6*ms)
# right(90)
# forward(2*ms)
# left(90)
# pd()
# for i in range(2):
#     forward(23*ms)
#     right(90)
#     forward(7 * ms)
#     right(90)
# pu()
# for x in range(0,100):
#     for y in range(0,100):
#         goto(x*ms,y*ms)
#         dot(5)
# done()
"""8"""
# from itertools import *
# a=product("ABCDE",repeat=4)
# b=[list(i) for i in a]
# count=0
# sogl=["B","C","D"]
# glas=["A","E"]
# for i in b:
#     if (i[-1]in sogl) and ((i[1]=="A" and i[0]!="A")  or (i[1]=="B" and i[0]!="B") or (i[1]=="C" and i[0]!="C")):
#         if ((i[2] in sogl) and (i[0] in glas)) or ((i[2] in glas) and (i[0] in sogl)):
#             count+=1
# print(count)
"""14"""
# def perevod(n,s):
#     string=''
#     while n>0:
#         string+=str(n%s)
#         n//=s
#     return string[::-1]
#
# a=[]
# sm=0
# for i in range(1,96):
#     tr=perevod(i,3)
#     pt=perevod(i,5)
#     if tr[-2:]=="21" and pt[0]=="3":
#         a.append(i)
# for i in a:
#     sm+=i
# print(sm)
"""15"""
# for a in range(1,501):
#     count=0
#     for r in range(1,501):
#         for x in range(1,501):
#             if (((x&108==0)or (x&60==0))<=(x&a==0))or (x&r==0):
#                 count+=1
#     if count==501*2:
#         print(a)
"""16"""
# def f(n):
#     if n<=2:
#         return 1
#     if n>2 and n%2!=0:
#         return f(n-1)-n
#     if n>2 and n%2==0 :
#         return f(n-2)+g(n-1)+2
#
# def g(n):
#     if n<=0:
#         return 2
#     if n>0 and n%2!=0:
#         return f(n-1)-2*g(n-2)
#     if n > 0 and n % 2 == 0:
#         return 2*f(n-2)-2*g(n-1)
# print(f(96))




