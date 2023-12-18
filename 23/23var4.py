def f(n,s):
    if n==s:
        return 1
    if n>s or n==21:
        return 0
    return f(n+2,s)+f(n+3,s)+f(n*5,s)
print(f(1,6)*f(6,35))



