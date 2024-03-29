"""2"""
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((x<=y) or (z==x)) and (w<=z):
#                     print(x,y,z,w)
"""5"""
# a=[]
# for n in range(1,1001):
#     r=bin(n)[2:]
#     r=r[::-1]
#     r+=r[-1]
#     if int(r,2)>99:
#         a.append(n)
# print(min(a))
"""8"""
# from itertools import *
# gl='еиа'
# sogl='вбнр'
# a=[list(i) for i in permutations('вебинар',r=7)]
# count=0
# for i in a:
#     for k in range(len(i)-1):
#         if ((i[k] in sogl) and (i[k+1] in sogl)) or ((i[k] in gl) and (i[k+1] in gl)):
#             break
#     else:
#         count+=1
# print(count)
"""9"""
# count=0
# for i in open('9-219.csv'):
#     a=list(map(int,i.split(';')))
#     nrp=sorted(a)[:-1]
#     f=1
#     for i in nrp:
#         f*=i
#     if (sum(sorted(a)[-2:])/sum(sorted(a)[:-2]))>2 and max(a)**2>f:
#         count+=1
# print(count)
"""13"""
# from ipaddress import *
# count=0
# net=ip_network('211.48.136.64/255.255.255.224',False)
# for i in net:
#     ln=bin(int(i))[2:]
#     if ln[-2:]=='11':
#         count+=1
# print(count)
"""16"""
# from sys import *
# from functools import *
#
# setrecursionlimit(10000)
# @lru_cache()
# def f(n):
#     if n<9:
#         return n//3+n%3
#     else:
#         return a[n//9]+a[n%9]
#
# a=[0]*(9**8+1)
# for i in range(len(a)):
#     a[i]=f(i)
# count=0
# for i in a:
#     if a[i]==33:
#         count+=1
# print(count)
"""17"""
# a=[int(i) for i in open('17-376.txt')]
# b=max([i for i in a if hex(i)[-2:]=='0f'])
# count=0
# mx=0
# for i in range(len(a)-1):
#     if ((a[i]%7==0 and a[i+1]%7!=0) or (a[i+1]%7==0 and a[i]%7!=0)) and (a[i]+a[i+1])%b==0:
#         count+=1
#         mx=max(mx,a[i]+a[i+1])
# print(count,mx)
"""24"""
a=open('24-204.txt').readline()
a=a[::-1]
a=a.replace('AA',"&").replace('CC','*')
a=a[::-1]
mx=0
count=0
for i in range(len(a)):
    if a[i]=='*' or a[i]=='&':
        count+=1
    else:
        mx=max(mx,count)
        count=0
print(mx)









