"""5"""
# for n in range(1,100001):
#     if n%2==0:
#         r=n//2
#     else:
#         r=n-1
#     if r%6==0:
#         r=r//6
#     else:
#         r=r-1
#     if r%15==0:
#         r=r//15
#     else:
#         r=r-1
#
#     if r==523:
#         print(n,hex(n)[2:])
"""8"""
# from itertools import *
# a=[list(i) for i in product('01234567',repeat=8)]
# count=0
# for i in a:
#     if int(i[0])%2==0 and int(i[-1])%2==0 and i[0]!='0':
#         for k in range(1,6):
#             if int(i[k])%2==1 and int(i[k+1])%2==1 and int(i[k+2])%2==1:
#                 count+=1
#                 break
# print(count)
"""9"""
# for i in open('v18.csv'):
#
#     while i[-1]==';':
#         i=i[:-1]
#     a=list(map(int,i.split(';')))
#     print(a)
"""14"""
# def f(n,s):
#     for i in range(len(n)):
#         n[i]=n[i]*s**(len(n)-1-i)
#     return sum(n)
# s=[]
# for x in range(16):
#     for y in range(16):
#         a=f([2,7,10,x,2,3],16)+f([8,y,14,5,int('d',16),2],16)
#         if a%5==0:
#             s.append(x+y)
# print(max(s))
"""15"""
# for a in range(1,500):
#     for x in range(1,500):
#         if ((((x & 103)==0) and ((x&94)!=0))<=((x&a)!=0))==0:
#             break
#     else:
#         print(a)
"""17"""
# a=[int(i) for i in open('17-366.txt')]
# m=min([i for i in a if str(abs(i))[-2:]=='68'])
# count=0
# mx=0
# for i in range(len(a)-1):
#     if (str(abs(a[i]))[-2:]=='68' and str(abs(a[i+1]))[-2:]!='68') or (str(abs(a[i]))[-2:]!='68' and str(abs(a[i+1]))[-2:]=='68'):
#         if a[i]**2 +a[i+1]**2>=m**2:
#             count+=1
#             mx=max(mx,a[i]**2 +a[i+1]**2)
# print(count,mx)
"""23"""
# def f(n,s):
#     if n==s:
#         return 1
#     if n<s or n==7:
#         return 0
#     return f(n-1,s)+f(n-3,s)+f(n//2,s)
# print(f(19,10)*f(10,3))
"""13"""
# from ipaddress import *
# '10011000'
# '10011101'
# print(int('11111000',2))
# """16"""
"""16"""
def f(n):
    if n==0:
        return 0
    else:
        return a[n-1]+5*n
a=[0]*(567654321+1)
for i in range(len(a)):
    a[i]=f(i)

count=0
for i in range(189456678,567654322):
    if a[i]%7!=0:
        count+=1
print(count)



