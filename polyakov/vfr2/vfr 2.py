"""2"""
"""4"""
"""7"""
"""11"""
"""12"""
mx=0
for n in range(4,1000):
    a='1'+'2'*n
    while '12' in a or '322' in a or '222' in a:
        if '12' in a :
            a=a.replace('12','2',1)
        if '322' in a:
            a=a.replace('322','21',1)
        if '222' in a :
            a=a.replace('222','3',1)
    mx=max(mx,a.count('2'))
print(mx)
"""5"""
# for n in range(1,1001):
#     r=bin(n)[2:]
#     if r.count('0') >0:
#         ind = r.rindex('0')
#         l = list(r)
#         l[ind] = ''.join(l[:2])
#         r=''.join(l)
#         r=r[::-1]
#     else:
#         continue
#     if int(r,2)==123:
#         print(n)
"""9"""
# for i in open('9-vfr2.csv'):
#     a=list(map(int,i.split(';')))
#     rp=[i for i in a if a.count(i)==2]
#     c=set(a)
#     if len(rp)==4 and len(c)==5 and rp.count(max(a))==0:
#         print(sum(a))
#         break
"""8"""""
# from itertools import *
# print([''.join(i) for i in product('аимря',repeat=4)].index('ария')+1)
"""13"""
# from ipaddress import *
# net=ip_network('216.130.64.0/255.255.192.0',False)
# count=0
# for i in net:
#     c=list(map(int,str(i).split('.')))
#     c=[i for i in range(len(c)) if c[i]%2==0]
#     if len(c)==4:
#         count+=1
# print(count)
"""14"""
# def perevod(n,s):
#     string=''
#     while n>0:
#         string+=str(n%s)
#         n//=s
#     return string[::-1]
# print(perevod(7*729**543-6*81**765-5*9**987-20,9).count('8'))
"""17"""
# b=[int(i) for i in open('17-384.txt')]
# mx=0
# for i in range(len(b)-1):
#     if (len(str(b[i]))==2 and len(str(b[i+1]))!=2) or (len(str(b[i]))!=2 and len(str(b[i+1]))==2):
#         mx=max(mx,b[i]+b[i+1])
# c=[i for i in b if i>mx]
# print(len(c),min(c))
"""24"""
# a=open('24-264 (1).txt').readline()
# sh='0123456789ABCDEF'
# count=1
# mx=0
# for i in range(len(a)-1):
#     if a[i] in sh and a[i+1] in sh:
#         count+=1
#     else:
#         mx=max(mx,count)
#         count=1
# print(mx)
"""25"""
# from fnmatch import *
# for i in range(1923,10**8,1923):
#     if fnmatch(str(i),'1*2??76'):
#         print(i,i//1923)
"""23"""
# def f(n,s):
#     if n==s:
#         return 1
#     if n>s:
#         return 0
#     return f(n+1,s)+f(n+3,s)+f(n+6,s)
# print(f(21,30))
"""16"""
# from sys import *
# setrecursionlimit(10000)
# def f(n):
#     if n<3:
#         return 3
#     else:
#         return 2*n+5+f(n-2)
# print(f(3027)-f(3023))









