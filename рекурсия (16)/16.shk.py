from sys import *
setrecursionlimit(10000)
def g(n):
    if n<2:
        return n
    if n>=2:
        return a[n//2]+a[n%2]

a=[0]*(100001)
count=0
for i in range(1,100001):
    a[i]=g(i)
for i in range(1,100001):
    print(a[i])
#     if a[i]==27:
#         count+=1
# print(count)


# def f(n):
#     if n==1:
#         return 1
#     if n==2:
#         return 3
#     if n>2:
#         return a[n-1]*n+a[n-2]*(n-1)
# a=[0]*6
# for i in range(1,6):
#     a[i]=f(i)
# print(a[5])