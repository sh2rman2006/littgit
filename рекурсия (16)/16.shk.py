from sys import *
setrecursionlimit(10000)
# def g(n):
#     if n<2:
#         return n
#     if n>=2:
#         return g(n//2)+g(n%2)
# count=0
# for i in range(100000):
#     if g(i)==27:
#         print(g(i))


def f(n):
    if n==1:
        return 1
    if n==2:
        return 3
    if n>2:
        return a[n-1]*n+a[n-2]*(n-1)
a=[0]*6
for i in range(1,6):
    a[i]=f(i)
print(a[5])