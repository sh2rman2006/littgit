def g(n,s):
    if n==s:
        return 1
    if n>s or n==16:
        return 0
    return g(n+3,s)+g(n+5,s)+g(n*2,s)


def f(n,s):
    if n==s:
        return 1
    if n>s or n==32:
        return 0
    return f(n+3,s)+f(n+5,s)+f(n*2,s)

print(g(4,32)*g(32,68)+f(4,16)*f(16,68))