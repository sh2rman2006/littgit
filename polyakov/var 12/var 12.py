"""5"""
# a=[]
# for n in range(1,1000001):
#     r=list(oct(n)[2:])
#     for i in range(len(r)):
#         if r[i] in '02468':
#             r[i]='1'
#     r=''.join(r)+str(n%8)
#     if int(r,8)%234==0:
#         a.append(int(r,8))
# print(max(a))
"""9"""
# count=0
# for i in open('9v12.csv'):
#     a=list(map(int,i.split(';')))
#     rp=[i for i in a if a.count(i)>1 and i!=min(a)]
#     if a.count(min(a))==1 and len(rp)>0 and (min(a)+max(a))<sum(rp):
#         count+=1
# print(count)
"""13"""
# from ipaddress import *
# net = ip_network('192.168.248.176/255.255.255.240',False)
# count=0
# for i in net :
#     ln=bin(int(i))[2:]
#     if ln.count('1')>ln.count('0'):
#         count+=1
# print(count)
"""14"""
# def f(n,s):
#     for i in range(len(n)):
#         n[i]=n[i]*s**(len(n)-1-i)
#     return sum(n)
#
# s=1
# for x in range(12):
#     for y in range(18):
#         a=f([6,7,x,x,3],12)+f([2,x,9,x],14)+f([4,4,x,x,3],15)-f([2,x,y,7],18)
#         if a>0 and a%77==0:
#             s*=(x*y)
# print(s)
"""16"""
# from sys import *
# setrecursionlimit(10000)
# def f(n):
#     if n>2:
#         return n+f(n-2)
#     else:
#         return n
# print(f(2023)+f(2020))
"""17"""
# a=[int(i) for i in open('17-374.txt')]
# ch=min([i for i in a if i%2==0])
# count=0
# mn=100000000
# for i in range(len(a)-2):
#     if (a[i]%2==0 and a[i+1]%ch==0 and a[i+2]%2==1) or (a[i+2]%2==0 and a[i+1]%ch==0 and a[i]%2==1):
#         count+=1
#         mn=min(mn,a[i]+a[i+2])
# print(count,mn)
"""19"""
def f(n,k):
    if n==4 and k>20:
        return 1
    if n==4 and k<21:
        return 0
    if n!=4 and k>20:
        return 0
    if n%2!=0:
        return f(n+1,k+1) or f(n+1,k*2)
    else:
        return f(n+1,k+1) and f(n+1,k*2)

for s in range(1,21):
    if f(1,s):
        print(s)











