
#28102
"""def F(n,s):
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

for i in range(1,65):
    if F(1,i):
        print(i)"""
#27823
"""def f(n,s):
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
for i in range(1,38):
    if f(1,i):
        print(i)"""

#3 кучи
"""def f(n,s1,s2,s3):
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
for i in range(1,58):
    if f(1,7,5,i):
        print(i)"""






