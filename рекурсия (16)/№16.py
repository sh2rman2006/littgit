#59757
"""import sys
from sys import *
sys.setrecursionlimit(10000)

def f(n):
    if n<11:
        return 10
    if n>=11:
        return n+f(n-1)
print(f(2024)-f(2022))"""
#58228
"""def f(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n>2 and n%2==0:
        return (4*n-f(n-3))//8
    if n>2 and n%2!=0:
        return( 4*n-f(n-1)+f(n-2))//8
print(f(52)-f(38))"""







