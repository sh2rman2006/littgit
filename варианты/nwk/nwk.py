"""5"""
# for n in range(1,10001):
#     r=bin(n)[2:]
#     if n%2==0:
#         r+=bin(r.count('1'))[2:]
#     else:
#         r='1'+r+'00'
#     if int(r,2)>215:
#         print(n);break
"""9"""
# for i in open('9_kkk.csv'):
#     a=list(map(int,i.split(';')))
"""14"""
# def f(n,s):
#     for i in range(len(n)):
#         n[i]=n[i]*s**(len(n)-1-i)
#     return sum(n)
#
# for x in range(26):
#     a=f([2,7,x,9,8,8,7,6],26)+f([2,6,x,5,1],26)+f([1,5,x,4,7],26)+f([6,2,x,5],26)
#     if a%25==0:
#         print(a//25)
"""17"""
# a=[int(i) for i in open('17_9164.txt')]
# b=max([i for i in a if i%17==0])
# count=0
# mx=0
# for i in range(len(a)-1):
#     if (a[i]+a[i+1])>b:
#         count+=1
#         mx=max(mx,a[i]+a[i+1])
# print(count,mx)





