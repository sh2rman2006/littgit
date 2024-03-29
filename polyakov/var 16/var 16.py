"""13"""
# '10011011'
# '10010001'
# print(int('11110000',2))
"""5"""
# def perevod(n,s):
#     m=[]
#     while n>0:
#         m.append(int(n%s))
#         n//=s
#     return m[::-1]
# def s(n, s):
#     c=[0]*len(n)
#     for i in range(len(n)):
#             c[i] = n[i] * s ** (len(n) - 1 - i)
#     return sum(c)
#
# a=[]
# for n in range(15,1001):
#     r=perevod(n,15)
#     if n%15==0:
#         r.append(r[0])
#         r.append(r[1])
#     else:
#         for k in perevod(n%15*13,15):
#             r.append(k)
#
#     if s(r,15)>700:
#         a.append(s(r,15))
# print(min(a))
"""9"""
# count=0
# for i in open('9-v16.csv'):
#     a=list(map(int,i.split(';')))
#     nrp=[i for i in a if a.count(i)==1]
#     rp=[i for i in a if a.count(i)>1]
#     if (len([i for i in a if a.count(i)==3])>0 and len(set(a))==4) and ((sum(nrp)/len(nrp))<sum(rp)):
#         count+=1
# print(count)
"""14"""
# def f(n,s):
#     for i in range(len(n)):
#         n[i]=n[i]*s**(len(n)-1-i)
#     return sum(n)
#
# for x in range(15):
#     a=f([6,7,8,4,5,x,6,5],15)+f([1,x,2,3,4,5,6],15)
#     if a%14==0:
#         print(a//14)
"""15"""
# for a in range(1,500):
#     flag=True
#     for x in [k*0.25 for k in range(-10000,10000)]:
#         b=160<=x<=180
#         f= b<=((x%35==0) <= (x%a==0))
#         if f!=1:
#             flag=False;break
#     else:
#         print(a)
"""16"""

