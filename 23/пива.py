
from sys import *
setrecursionlimit(10000)

from math import *



#поляков 6555
def p(n):
    if gcd(n,n+1)==1:
         return n+1
def r(n):
    if gcd(n, n + 3) == 1:
        return n + 3
def g(n):
    n=int(n)
    if gcd(n,n+7)==1:
         return n+7
def f(n,s):
    if n==s:
        return 1
    if n>s :
        return 0
    return f(p(n),s)+f(r(n),s)+f(g(n),s)
print(f(13,31))


print(type(gcd(12,24)))

