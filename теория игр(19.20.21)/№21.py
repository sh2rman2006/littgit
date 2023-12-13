
#28102
"""def G(n,s):
    if (n==5 or n==3) and s>=65:
        return 1
    if n==5 and s<65:
        return 0
    if n<5 and s>=65:
        return 0
    if n%2==0:
        return G(n+1,s+1) or G(n+1,s*2)
    else:
        return G(n+1,s+1) and G(n+1,s*2)

def F(n,s):
    if n==3 and s>=65:
        return 1
    if n<3 and s>=65:
        return 0
    if n==3 and s<65:
        return 0
    if n%2==0:
        return F(n+1,s+1) or F(n+1,s*2)
    else:
        return F(n+1,s+1) or F(n+1,s*2)
a=set()
b=set()
for i in range(1,68):
    if F(1,i):
        a.add(i)
for i in range(1,68):
    if G(1,i):
        b.add(i)
print(a&b)
"""
#27825
"""def k(n,s):
    if (n==5 or n==3) and s>=38:
        return 1
    if n==5 and s<38:
        return 0
    if n<5 and s>=38:
        return 0
    if n%2==0:
        return k(n+1,s+1) or k(n+1,s+2) or k(n+1,s*2)
    else:
        return k(n+1,s+1) and k(n+1,s+2) and k(n+1,s*2)
def f(n,s):
    if n==3 and s>=38:
        return 1
    if n==3 and s<38:
        return 0
    if n<3 and s>=38:
        return 0
    if n%2==0:
        return f(n+1,s+1)or f(n+1,s+2)or f(n+1,s*2)
    else:
        return  f(n+1,s+1)or f(n+1,s+2)or f(n+1,s*2)
a=set()
b=set()
for i in range(1,38):
    if k(1,i):
        a.add(i)
for i in range(1,38):
    if f(1,i):
        b.add(i)
print(a&b)
"""
#
"""def f(n,s1,s2,s3):
    if (n==3 or n==5) and s1+s2+s3>=71:
        return 1
    if n == 5 and s1 + s2 + s3 < 71:
        return 0
    if n < 5 and s1 + s2 + s3 >= 71:
        return 0
    if n%2==0:
        return f(n+1,s1+3,s2,s3) or f(n+1,s1*2,s2,s3) or f(n+1,s1,s2+3,s3)or f(n+1,s1,s2*2,s3) or f(n+1,s1,s2,s3+3) or f(n+1,s1,s2,s3*2)
    else:
        return f(n+1,s1+3,s2,s3) and f(n+1,s1*2,s2,s3) and f(n+1,s1,s2+3,s3)and f(n+1,s1,s2*2,s3) and f(n+1,s1,s2,s3+3) and f(n+1,s1,s2,s3*2)

a=set()
for i in range(1,58):
    if f(1,7,5,i):
        a.add(i)


def f(n,s1,s2,s3):
    if n==3 and s1+s2+s3>=71:
        return 1
    if n == 3 and s1 + s2 + s3 < 71:
        return 0
    if n < 3 and s1 + s2 + s3 >= 71:
        return 0
    if n%2==0:
        return f(n+1,s1+3,s2,s3) or f(n+1,s1*2,s2,s3) or f(n+1,s1,s2+3,s3)or f(n+1,s1,s2*2,s3) or f(n+1,s1,s2,s3+3) or f(n+1,s1,s2,s3*2)
    else:
        return f(n+1,s1+3,s2,s3) or f(n+1,s1*2,s2,s3) or f(n+1,s1,s2+3,s3)or f(n+1,s1,s2*2,s3) or f(n+1,s1,s2,s3+3) or f(n+1,s1,s2,s3*2)
b=set()
for i in range(1,58):
    if f(1,7,5,i):
        b.add(i)
print(a&b)
"""
