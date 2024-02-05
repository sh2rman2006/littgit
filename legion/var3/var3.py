"""9"""
# count=0
# for i in open("9.var3.csv"):
#     a=list(map(int,i.split(";")))
#     sr=[x for x in a if x!=max(a) and x!=min(a)]
#     if a.count(max(a))>1:
#         for l in range(a.count(max(a))-1):
#             sr.append(max(a))
#     if a.count(min(a))==2:
#         for l in range(a.count(min(a)) - 1):
#             sr.append(min(a))
#     sr2=2*sum(sr)
#     if (max(a)+min(a))<sr2:
#         count+=1
# print(count)
"""17"""
# a=open("17.txt")
# b=[int(i) for i in a]
# mn=min(b)
# d=[i for i in b if i%4==0]
# d=sum(d)/len(d)
# count=0
# sm=-10000000000000
# for i in range(len(b)-1):
#     if (b[i]+b[i+1])<d and (b[i]%mn==0 or b[i+1]%mn==0):
#         sm=max(sm,b[i]+b[i+1])
#         count+=1
# print(sm,count)
"""24"""
# a=open("24.txt").readline()
# mx=-100000000000
# for i in range(len(a)):
#     if a[i]=="A":
#         c=0
#         v=1
#         for k in range(i+1,len(a)):
#             if a[k]=="A":
#                 v+=1
#             else:
#                 c+=1
#             if v==3:
#                 c+=1
#                 mx=max(mx,c)
#                 break
# print(mx)
"""23"""
# def f(n,s):
#     if n==s:
#         return 1
#     if n>s:
#         return 0
#     return f(n+1,s)+f(n*3,s)
#
# print(f(1,11)*f(11,34))
"""16"""
# def f(n):
#     if n<=1:
#         return 1
#     if n==2:
#         return 2
#     if n>2 and n%3==0:
#         return 2*n-f(n//3)-f(n-1)
#     if n>2 and n%3!=0:
#         return n+f(n-2)+f(n//10)
# count=0
# for i in range(50,101):
#     if 50<f(i)<=200:
#         count+=1
# print(count)
"""15"""
# for a in range(1,1001):
#     count=0
#     for x in range(1,1001):
#         if ((x%a!=0)<=((x%27==0)<=(x%89!=0)))and (a>300):
#             count+=1
#     if count==1000:
#         print(a)
"""14"""
# for x in range(13):
#     a=(1*13**4+8*13**3+6*13**2+x*13+4*13**0)+(5*13**4+x*13**3+7*13**2+1*13**1+6*13**0)
#     if a%11==0:
#         # print(a/11)
"""13"""
# from ipaddress import *
# for mask in range(32):
#     net=ip_network(f"172.49.54.172/{mask}",False)
#     if str(net.network_address)=="172.49.48.0":
#         print(mask)
# print(int("11111000",2),"///")
"""12"""
# a=">"+15*"2"+20*"3"+25*"5"
# while ('>2' in a) or ('>3' in a) or ('>5' in a):
#     if ('>2' in a) :
#         a=a.replace(">2",'333>',1)
#     if ('>3' in a) :
#         a=a.replace(">3",'23>',1)
#     if ('>5' in a) :
#         a=a.replace(">5",'35>',1)
# sm=0
# for i in range(len(a)-1):
#     sm+=int(a[i])
# print(sm)
"""8"""
# from itertools import *
# a=product("EKOR",repeat=6)
# b=[list(i) for i in a]
# x=0
# for i in range(len(b)):
#     x+=1
#     v=True
#     if b[i][0]=="O":
#         if (b[i][1]=="E" and b[i][2]=="E") or (b[i][2]=="E" and b[i][3]=="E") or (b[i][3]=="E" and b[i][4]=="E")\
#             or (b[i][4]=="E" and b[i][5]=="E"):
#             v=False
#         if v:
#             print(x)
#             break
"""5"""
# for n in range(1,1001):
#     r=bin(n)[2:]
#     if n%2==0:
#         r+="01"
#     else:
#         r="1"+r+"10"
#     if int(r,2)>214:
#         print(n)
#         input()











