from sys import *
setrecursionlimit(10000)

from math import *

#поляков 6555
def l(n):
    if gcd(n,n+1)==1:
         return n+1
    return n
def r(n):
    if gcd(n, n + 3) == 1:
        return n + 3
    return n
def g(n):
    if gcd(n,n+7)==1:
         return n+7
    return n
def f(n,s):
    if n==s:
        return 1
    if n>s :
        return 0
    return f(l(n),s)+f(r(n),s)+f(g(n),s)
# print(f(13,31))



