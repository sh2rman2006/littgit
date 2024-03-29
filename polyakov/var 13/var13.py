"""2"""
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((x or y or z)<=(x and (y or w)))==0:
#                     print(x,y,z,w)
"""15"""
# for x in [k*0.25 for k in range(-10000,10000)]:
#     a=0
#     b=10<=x<=40
#     f=a or (b<=(x%6!=0))
#     if f!=1:
#         print(x)
"""5"""
# for n in range(11,10001):
#     r=oct(n)[2:]
#     if n%5==0:
#         r+=r[:3]
#     else:
#         r+=bin(n%5)[2:]
#     if int(r,8)>=35000:
#         print(n);break
"""9"""
# count=0
# for i in open('9vv13.csv'):
#     a=list(map(int,i.split(';')))
#     rp=[i for i in a if i!=max(a) and a.count(i)>1]
#     if a.count(max(a))==1 and len(rp)>0 and sum(rp)<(max(a)+min(a)):
#         count+=1
# print(count)
"""8"""
# from itertools import *
# count=0
# gl='оеэ'
# sogl='кмпг'
# a=[list(i) for i in product('компегэ',repeat=6)]
# for i in a:
#     if (i[0] in gl) and (i[-1]in gl):
#         for k in range(1,5):
#             if i[k] in gl:
#                 break
#         else:
#             count+=1
# print(count)
"""13"""
# from ipaddress import *
# count=0
# net=ip_network('192.168.248.176/255.255.255.240',False)
# for i in net:
#     ln=bin(int(i))[2:]
#     if ln.count('1')==ln.count('0'):
#         count+=1
# print(count)
"""14"""
# def f(n,s):
#     for i in range(len(n)):
#         n[i]=n[i]*s**(len(n)-1-i)
#     return sum(n)
#
# for x in range(22):
#     a=f([1,8,x,8,9,9,5,7],22)+f([8,0,x,3,3],22)+f([5,2,1,x,6],22)
#     if a%21==0:
#         print(a//21)
"""16"""
# from sys import *
# setrecursionlimit(10000)
# def f(n):
#     if n==1:
#         return 1
#     else:
#         return n*f(n-2)
#
# print(f(2023)/f(2019))
"""17"""
def perevod(n,s):
    string=''
    while n>0:
        string+=str(n%s)
        n//=s
    return string[::-1]

file=[int(i) for i in open('17-370.txt')]
m=max([i for i in file if len(str(abs(i)))==3 and perevod(i,3)==perevod(i,3)[::-1]])
print(m)


