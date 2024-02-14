"""5"""
# for n in range(1000,10000):
#     a=set(list(str(n)))
#     if len(a)==4:
#         s = list(map(int, str(n)))
#         sm = max(s) + min(s)
#         b = [i for i in s if i != max(s) and i != min(s)]
#         pr=1
#         for i in b:
#             pr*=i
#         r=[]
#         r.append(sm)
#         r.append(pr)
#         r.sort()
#         r=''.join(map(str,r))
#         if int(r)>85:
#             print(n)
#             break
"""7"""
# 81921
"""8"""
# from itertools import *
# gl='ИЕОА'
# sogl='ГПРБЛ'
# count=0
# b=[list(i) for i in product('ГИПЕРБОЛА',repeat=6)]
# for i in b:
#     if (i[0] in sogl) and (i[-1] in sogl):
#         flag=True
#         for k in range(len(i)-2):
#             if (i[k+1] in gl) and (i[k] in sogl and i[k+2] in sogl):
#                 flag=False
#         if flag:
#             count+=1
# print(count)
"""13"""
# c0='000'
# c1='111'
# from ipaddress import *
# count=0
# a=ip_network('212.192.32.118/255.255.255.224',False)
# for i in a:
#     ln=bin(int(i))[2:]
#     if (c0 not in ln[-8:]) and (c1 not in ln[-8:]):
#         count+=1
# print(count)
"""16"""
# def f(n):
#     if n<=1:
#         return 1/2
#     else:
#         return (n+1)*f(n-1)
# print(f(200)/f(198))
"""14"""
# a='0123456789abcd'
# mx=0
# for x in a:
#     for y in a:
#         ar=int(f'14{y}5{x}2',14)+int(f'31{x}2{y}3',14)
#         if ar%9==0:
#             mx=max(ar//9,mx)
# print(mx)





