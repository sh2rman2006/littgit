#27391
def f(n,s=30):
    if n==s:
        return 1
    if n>s:
        return 0
    return f(n*2,s)+ f(n+2,s)
print(f(1,14)*f(14,30))




