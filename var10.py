# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if(((z<=y)<=x)or (not w))==0:
#                     print(x,y,z,w)

# 1w 2y 3z 4x

#5
# for n in range(100,1000):
#     r=str(n)
#     f1=int(r[0])**2+int(r[1])**2
#     f2=int(r[1])**2+int(r[2])**2
#     if f1>f2:
#         s=str(f1)+str(f2)
#     else:
#         s = str(f2) + str(f1)
#     if s=="7434":
#         print(n)

#8

#12
# a="1"*2022
# while ("11" in a) or ("555" in a):
#     if "11" in a:
#         a=a.replace("11","555")
#     elif "555" in a:
#         a=a.replace("555","5")
# print(a)
#14
# a= 4**2022-2*4**1111+16**600+192
# def perevod(n,s):
#     string=''
#     while n>0:
#         string+=str(n%s)
#         n//=s
#     return string[::-1]
# print(perevod(a,4).count("3"))

#16
# from sys import *
# setrecursionlimit(10000)
# def f(n):
#     if n==1:
#         return 1
#     if n>1:
#         return n**2+f(n-1)
# print(f(2023)-f(2019))

#19
# def f(n,s):
#     if n==3 and s>176:
#         return 1
#     if n==3 and s<177:
#         return 0
#     if n<3 and s>176:
#         return 0
#     if n%2==0:
#         return f(n+1,s+1) or f(n+1,s*2)
#     else:
#         return f(n+1,s+1) and f(n+1,s*2)
# for s in range(1,177):
#     if f(1,s):
#         print(s)
#20
# def f(n,s):
#     if n==4 and s>176:
#         return 1
#     if n==4 and s<177:
#         return 0
#     if n<4 and s>176:
#         return 0
#     if n%2!=0:
#         return f(n+1,s+1) or f(n+1,s*2)
#     else:
#         return f(n+1,s+1) and f(n+1,s*2)
# for s in range(1,177):
#     if f(1,s):
#         print(s)

#21
# def f(n,s):
#     if (n==3 or n==5) and s>176:
#         return 1
#     if n==5 and s<177:
#         return 0
#     if n<5 and s>176:
#         return 0
#     if n%2==0:
#         return f(n+1,s+1) or f(n+1,s*2)
#     else:
#         return f(n+1,s+1) and f(n+1,s*2)
# a=set()
# for s in range(1,177):
#     if f(1,s):
#         print(s)
#         a.add(s)
# print("///////////////////")
#
# def f(n,s):
#     if n==3 and s>176:
#         return 1
#     if n==3 and s<177:
#         return 0
#     if n<3 and s>176:
#         return 0
#     if n%2==0:
#         return f(n+1,s+1) or f(n+1,s*2)
#     else:
#         return f(n+1,s+1) and f(n+1,s*2)
# b=set()
# for s in range(1,177):
#     if f(1,s):
#         print(s)
#         b.add(s)
# print(a-b)
#23
# def f(n,s):
#     if n==s :
#         return 1
#     if n>s:
#         return 0
#     return f(n+2,s)+f(n+7,s)
# print(f(7,51))
#25
# for  i in range(860000,10000000):
#     mi=100000
#     ma=-100000
#     for d in range(2,i-1):
#         if i%d==0:
#             mi=min(mi,d)
#             ma=max(ma,d)
#     m=ma-mi
#     if str(m)[-2:]=="30":
#         print(i,m)

#6
# from turtle import *
# a=Screen()
# a.screensize(10000,10000)
#
# left(90)
# ms=25
# tracer(0)
# for i in range(10):
#     forward(7*ms)
#     right(120)
# pu()
# for x in range(-10,51):
#     for y in range(-10,51):
#         goto(x*ms,y*ms)
#         dot(5)
# done()
#13

from ipaddress import *
for i in range(1,9):
    c=int('1'*i+'0'*(8-i),2)
    a=ip_network(f"199.59.129.3/255.255.{c}.0",False)
    for i in a:
        s=bin(int(i))[2:]
        if (s[:-16].count("1")>=s[-16:].count("1"))==False:
            break
    else:
        print(c)

# from ipaddress import *
# for i in range(1, 9):
#     a = int('1'*i + '0'*(8-i), 2)
#     net = ip_network(f'199.59.129.3/255.255.{a}.0', False)
#     for j in net:
#         p = bin(int(j))[2:]
#         if (p[:-16].count('1') >= p[-16:].count('1')) == False:
#             break
#     else:
#         print(a)