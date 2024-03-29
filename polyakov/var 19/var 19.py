"""5"""
# otv=[]
# for n in range(1,10001):
#     r=oct(n)[2:]
#     if len(r)==4:
#         a=int(str(n)[0])+int(str(n)[-1])
#         b=int(str(n)[1])+int(str(n)[2])
#         c=sorted([a,b])
#        c=''.join(map(str,c))
#         print(c)
#         if c=='317':
#             otv.append(n)
#
# print()
"""9"""
# count=0
# for i in open('v19.csv'):
#     a=list(map(int,i.split(';')))
#     print(a)
#     if len(set(a))==4:
#         if sum([i for i in a if a.count(i)>1])>sum([i for i in a if a.count(i)==1]):
#             count+=1
#
# print(count)
"""13"""
# from ipaddress import *
# '01001001'
# '01001011'
# print(int('11111100',2))
"""16"""
# from sys import *
# setrecursionlimit(10000)
# def f(n):
#     if n==0:
#         return 0
#     else:
#         return a[n-1]+2*n
#
# count=0
#
# a=[0]*200000001*2
# for i in range(len(a)):
#     a[i]=f(i)
# for n in range(100000000,200000001):
#     if a[n]%3!=0:
#         count+=1
# print(count)
"""17"""
a=[int(i) for i in open('17-365.txt')]
m=0
for i in range(len(a)-1) :
    if (str(a[i])[-1]=='1' and str(a[i+1])[-1]!='1') or (str(a[i])[-1]!='1' and str(a[i+1])[-1]=='1'):
        m=max(m,(a[i]+a[i+1])/2)

count=0
mx=0
mn=100000000
for i in range(len(a)-1) :
    if (str(a[i])[-1]=='1' and str(a[i+1])[-1]!='1') or (str(a[i])[-1]!='1' and str(a[i+1])[-1]=='1'):
        if a[i]<m and a[i+1]<m:
            count+=1
            if min(a[i],a[i+1])<mn:
                mn=min(a[i],a[i+1])
                mx=max (a[i],a[i+1])
print(count,mx)


