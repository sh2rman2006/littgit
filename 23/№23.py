#3607
"""def prib(n,s=50):
    if n>s:
        return 0
    if n==s:
        return 1
    return prib(n+2) + prib(n*5)
print(prib(2))"""
#6997
"""def pr(n,s=15):
    if n>s:
        return 0
    if n==s:
        return 1
    return pr(n+1) +pr(n*2)+pr(n*2+1)+pr(n*10)
print(pr(1))"""
#15117
"""def pr(n,s=20):
    if n > s or n==15:
        return 0
    if n == s:
        return 1
    return pr(n+1,s)+pr(n+2,s)
print(pr(3,9)*pr(9,20))"""
#33768
"""def f(n,s=16):
    if n > s or n == 15:
        return 0
    if n == s:
        return 1
    return f(n+1,s) + f(n+2,s) + f(n*3,s)
print(f(2,11)*f(11,16))"""
#15932
"""def f(n,s):
    if n>s or n==29:
        return 0
    if n==s:
        return 1
    return f(n+1,s)+f(n*2,s)+f(n*3,s)
print(f(2,13)*f(13,44))"""

