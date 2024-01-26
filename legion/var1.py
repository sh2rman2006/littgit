"""2"""
# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (not(x==z))and (not(w<=(y and z))):
#                     print(x,y,z,w)
# 1y 2x 3w 4z
"""5"""
# for n in range(1,200):
#     r=bin(n)[2:]
#     if r.count("1")%2==0:
#         r+="10"
#         r="110"+r[3:]
#     else:
#         r+="101"
#         r="10"+r[2:]
#     if int(r,2)>120:
#         print(n)
"""7"""
#14
"""8"""
# from itertools import *
# a=product("0123456",repeat=5)
# b=[list(i) for i in a]
# count=0
# for i in b:
#     if i[0]!="0" and i.count("4")==1:
#         if i.index("4")>0 and i.index("4")<4:
#             if int(i[i.index("4")-1])%2==0 and int(i[i.index("4")+1])%2==0:
#                 count+=1
#         if i.index("4")==0:
#             if int(i[1])%2==0:
#                 count+=1
#         if i.index("4")==4:
#             if int(i[3])%2==0:
#                 count+=1
# print(count)
"""11"""
# otv=2898
"""12"""
# for n in range(1,10000):
#     a=">"+31*"0"+n*"1"+47*"2"
#     while (">1" in a) or (">2" in a) or  (">0" in a):
#         if ">1" in a:
#             a=a.replace(">1","21>",1)
#         if ">2" in a:
#             a=a.replace(">2","12>",1)
#         if ">0" in a:
#             a=a.replace(">0","2>",1)
#     sum=a.count("1")+a.count("2")*2
#     der=0
#     for d in range(2,int(sum**0.5)+1):
#         if sum%d==0:
#             der+=1
#     if der==0:
#         print(n)
"""13"""
# from ipaddress import *
# for mask in range(32):
#     a=ip_network(f"185.49.83.72/{mask}",False)
#     if str(a.network_address)=="185.49.80.0":
#        print(mask)
#        print(int("11110000",2))
"""14"""
# for x in range(13):
#     a=(2*13**4+6*13**2+x*13+9)+(3*13**4+x*13**3+2*13+7)-(x*13**2+5*13+2)
#     if a%11==0:
#         print(a//11)
"""15"""
# for a in range(1,301):
#     count=0
#     for x in range(1,301):
#         if (x&56!=0)<=((x&a==0)<=(x&35!=0)):
#             count+=1
#     if count==300:
#         print(a)
"""16"""
# from sys import *
# setrecursionlimit(10000)
# def f(n):
#     if n==1:
#         return 1
#     if n==2:
#         return 3
#     if n>2:
#         return a[n-1]+n*a[n-2]
#
# a=[0]*1891
# for i in range(1,1891):
#     a[i]=f(i)
# print(a[1890]/a[1885])
"""17"""
# a=open("17.1.txt")
# maxs=0
# count=0
# fer=0
# b=[int(i)for i in a]
# for i in b:
#     if len(str(i)) == 3 and str(i)[-1] == "4":
#         fer=max(fer,i)
#
#
# for i in range(len(b)-1):
#     if (str(b[i])[-1]=="3" and str(b[i+1])[-1]!="3") or( str(b[i])[-1]!="3" and str(b[i+1])[-1]=="3"):
#         if (b[i]+b[i+1])%fer!=0:
#             count+=1
#             maxs=max(maxs,b[i]+b[i+1])
# print(maxs,count)
"""19"""
# def f(n,s):
#     if n==3 and s>=122:
#         return 1
#     if n==3 and s<122:
#         return 0
#     if n<3 and s>=122:
#         return 0
#     if n%2==0:
#         return f(n+1,s+1) or f(n+1,s+3) or f(n+1,s*5)
#     else:
#         return f(n + 1, s + 1) and f(n + 1, s + 3) and f(n + 1, s * 5)
# for s in range(1,122):
#     if f(1,s):
#         print(s)
"""20"""
# def f(n,s):
#     if n==4 and s>=122:
#         return 1
#     if n==4 and s<122:
#         return 0
#     if n<4 and s>=122:
#         return 0
#     if n%2!=0:
#         return f(n+1,s+1) or f(n+1,s+3) or f(n+1,s*5)
#     else:
#         return f(n + 1, s + 1) and f(n + 1, s + 3) and f(n + 1, s * 5)
# for s in range(1,122):
#     if f(1,s):
#         print(s)
"""21"""
# def f(n,s):
#     if (n==3 or n==5) and s>=122:
#         return 1
#     if n==5 and s<122:
#         return 0
#     if n<5 and s>=122:
#         return 0
#     if n%2==0:
#         return f(n+1,s+1) or f(n+1,s+3) or f(n+1,s*5)
#     else:
#         return f(n + 1, s + 1) and f(n + 1, s + 3) and f(n + 1, s * 5)
# for s in range(1,122):
#     if f(1,s):
#         print(s)
# print("////")
# def f(n,s):
#     if n==3 and s>=122:
#         return 1
#     if n==3 and s<122:
#         return 0
#     if n<3 and s>=122:
#         return 0
#     if n%2==0:
#         return f(n+1,s+1) or f(n+1,s+3) or f(n+1,s*5)
#     else:
#         return f(n + 1, s + 1) and f(n + 1, s + 3) and f(n + 1, s * 5)
# for s in range(1,122):
#     if f(1,s):
#         print(s)
"""23"""
# def f(n,s):
#     if n==s:
#         return 1
#     if n>s or n==11:
#         return 0
#     return f(n+1,s)+f(n*2,s)+f(n*3,s)
# print(f(5,19)*f(19,39))
"""24"""
# a=open("24.1.txt").readline()
# b=["A","B","C","D"]
# c="C"
# count=1
# maxco=0
#
# for i in range(len(a)-1):
#     if (a[i] in b) and (a[i+1] in b):
#         if (a[i]=="C" and a[i+1]=="C"):
#             maxco=max(maxco,count)
#             count=1
#         else:
#             count+=1
#     else:
#         maxco = max(maxco, count)
#         count = 1
# print(maxco)

