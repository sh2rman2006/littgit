"""1"""
"""2"""
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (x<=y)and (y or z) and w:
#                     print(x,y,z,w)
"""5"""
# for n in range(1,1001):
#     r=bin(2*n)[2:]
#     r+=str(r.count('1')%2)
#     r += str(r.count('1') % 2)
#     if int(r,2)>123:
#         print(n)
#         break
"""7"""
# from itertools import *
# b=[list(i) for i in product('АБВГДЕ',repeat=5)]
# count=0
# for i in b:
#     if i[-1]=="Е" and i.count('А')>0:
#         for k in range(len(i)-2):
#             if i[k]==i[k+2]:
#                 break
#         else:
#             count+=1
# print(count)
"""9"""
"""13"""
# from ipaddress import *
# for mask in range(32):
#     net=ip_network(f'168.92.235.17/{mask}',False)
#     if str(net.network_address)=='168.92.224.0':
#         print(mask)
"""14"""
# def perevod(n,s):
#     string=''
#     while n>0:
#         string+=str(n%s)
#         n//=s
#     return string[::-1]
# print(perevod(5**200+25**1000-5**50,5).count('0'))
"""15"""
# for z in range(-200,301):
#     flag=True
#     for x in range(-200,301):
#         if ((x+(z+1)>0)<=((x-7<=0)<= (x+7<=0)))==0:
#             flag=False
#     if flag:
#         print(z)
"""16"""
# def f(n):
#     if n==2 or n==1:
#         return 2
#     if n>2 and n%3!=0:
#         return 3*f(n-3)
#     else:
#         return n+2*f(n-1)
# print(f(27))
"""17"""
#count=0
# mx=-100000000
# b=[int(i) for i in open('17_var9.txt')]
# for i in range(len(b)-1):
#     if b[i]>b[i+1]:
#         mx=max(mx,b[i]-b[i+1])
#         count+=1
# print(count,mx)
"""24"""
# a=open('24_var9.txt').readline()
# for i in range(len(a)-2):
"""25"""









