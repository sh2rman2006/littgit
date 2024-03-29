"""2"""
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((not y) and (x<=((not z)==w))or z)==0:
#                     print(x,y,z,w)
# 1y 2x 3w 4z
"""5"""
# def perevod(n,s):
#     string=''
#     while n>0:
#         string+=str(n%s)
#         n//=s
#     return string[::-1]
# a=[]
# for n in range(11,1001):
#     r=perevod(n,3)
#     ch=[int(i) for i in r if int(i)%2==0]
#     nch=[int(i) for i in r if int(i)%2==1]
#     if len(ch)>len(nch):
#         r='22'+r
#     else:r='11'+r
#     if int(r,3)>100:
#         a.append(int(r,3))
# print(min(a))
"""8"""
# from itertools import *
# print(len(set([''.join(i) for i in permutations('биткоин',len('биткоин'))])))
"""9"""
# count=0
# for i in open('9v14.csv'):
#     a=list(map(int,i.split(';')))
#     rp=[i for i in a if a.count(i)>1]
#     if a.count(min(a))==1 and len(rp)>0 and (max(a)+min(a))<(2*(sum(sorted(a)[1:5])/4)):
#         count+=1
# print(count)
"""13"""
# from ipaddress import *
# count=0
# net=ip_network('192.168.32.160/255.255.255.240',False)
# for i in net:
#     ln=bin(int(i))[2:]
#     if ln.count('1')%2==0:
#         count+=1
# print(count)
"""14"""
# def f(n,s):
#     for i in range(len(n)):
#         n[i]=n[i]*s**(len(n)-1-i)
#     return sum(n)
#
# for x in range(19):
#     a=f([9,8,x,7,9,6,4,1],19)+f([3,6,x,1,4],19)+f([7,3,x,4],19)
#     if a%18==0:
#         print(a//18)
"""15"""
# for x in [k*0.25 for k in range(-10000,10000)]:
#     a=0
#     b=20<=x<=80
#     f= b<=((x%17==0)<=a)
#     if f!=1:
#         print(x)
"""16"""
# from sys import *
# setrecursionlimit(10000)
# def f(n):
#     if n==1:
#         return 1
#     else:
#         return n+f(n-1)
# print(f(2023)-f(2019))
"""17"""
# a=[int(i) for i in open('17-370.txt')]
# mn=min([i for i in a if len(str(abs(i)))==3 and str(abs(i))==str(abs(i))[::-1]])
# count=0
# mx=0
# for i in range(len(a)-1):
#     if (len(str(abs(a[i])))==4 and  len(str(abs(a[i+1])))!=4) or (len(str(abs(a[i])))!=4 and  len(str(abs(a[i+1])))==4):
#         if (a[i]**2+a[i+1]**2)%mn==0:
#             count+=1
#             mx=max(mx,a[i]**2+a[i+1]**2)
# print(count,mx)
"""23"""
a=[]
def f(n,k):
    if k==12:
        a.append(n)
        return 1
    if k>12:
        return 0
    return f(n+1,k+1)+f(n*2-3,k+1)

f(3,0)
print(len(set(a)))




