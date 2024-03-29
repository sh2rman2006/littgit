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
for x in range(23):
    a=[7,x,3,8,5,9,6]
    b=[1,4,x,3,6]
    c=[6,1,x,7]
    for i in range(len(a)):
        a[i]=i*23**(len(a)-1-i)
    a=sum(a)
    for i in range(len(b)):
        b[i]=i*23**(len(b)-1-i)
    b=sum(b)
    for i in range(len(c)):
        c[i]=i*23**(len(c)-1-i)
    c=sum(c)
    s=a+b+c
    if s%22==0 :
        print(s)
        a=[]
        b=[]
        c=[]
        break









