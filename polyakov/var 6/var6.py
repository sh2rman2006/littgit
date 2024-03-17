"""2"""
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((x and (not y)) or (x==z) or w)==0:
#                     print(x,y,z,w)
# 1y 2x 3w 4z
"""5"""
# a=[]
# for n in range(1,1001):
#     r=bin(n)[2::]
#     s=r.count('1')
#     if s%2==0:
#         r+=r[-2:]
#     else:
#         r+=r[-2:][::-1]
#     if int(r,2)>154:
#         a.append(n)
# print(min(a))
"""8"""
# from itertools import *
# a=[''.join(i) for i in product('екмопртью',repeat=5)]
# for i in range(len(a)):
#     if (i+1)%2!=0 and a[i][0]!='ь' and a[i].count('к')==2:
#         print(i+1)
"""9"""
# count=0
# for i in open('9-pol6.csv'):
#     a=list(map(int,i.split(';')))
#     s=sum([i for i in a if i!=max(a)])
#     rp=[i for i in a if a.count(i)==2]
#     for k in range(a.count(max(a))-1):
#         s+=max(a)
#     if len(rp)==2 and s>max(a):
#         count+=1
# print(count)
"""13"""
# from ipaddress import *
# count=0
# net=ip_network('202.75.38.152/255.255.255.248',False)
# for i in net:
#     ln=bin(int(i))[2:]
#     if ln.count('111')>0:
#         count+=1
# print(count)
"""16"""
# from sys import *
# def f(n):
#     if n>=2022:
#         return n
#     else:
#         return f(n+5)+7
# print(f(45)-f(49))
"""17"""
# a=[int(i) for i in open('17-380.txt')]
# s=max([i for i in a if str(i)[-2:]=='25'])
# count=0
# mx=0
# for i in range(len(a)-2):
#     k=0
#     if len(str(abs(a[i])))==4:
#         k+=1
#     if len(str(abs(a[i+1])))==4:
#         k+=1
#     if len(str(abs(a[i+2])))==4:
#         k+=1
#     if k!=3 and (a[i]+a[i+1]+a[i+2])<=s:
#         count+=1
#         mx=max(mx,a[i]+a[i+1]+a[i+2])
# print(count,mx)
""""24"""
# mx=0
# count=0
# # s=['AB','AC',"AD",'OB','OC','OD','BA','BO','CA','CO','DA','DO']
# a=open('24-212 (1).txt').readline()
# for i in range(len(a)):
#     if (a[i] in 'BCD' and count%2==1) or (a[i] in 'AO' and count%2==0):
#         count+=1
#     else:
#         mx=max(mx,count)
#         count=0
# print(mx)
"""25"""
# from fnmatch import *
# for i in range(4013,10**12,4013):
#     if fnmatch(str(i),'123?4*5679'):
#         print(i,i/4013)
"""23"""
# def f(n,s):
#     if n==s:
#         return 1
#     if n>s or str(n).count('5')>0:
#         return 0
#     return f(n+1,s)+f(n+3,s)+f(n*3,s)
# print(f(1,49))
""""14"""
# def perevod(n,s):
#     string=''
#     while n>0:
#         string+=str(n%s)
#         n//=s
#     return string[::-1]
# a=4*625**1920+4*125**1930-4*25**1940-3*5**1950-1960
# print(perevod(a,5).count('0'))
"""7"""













