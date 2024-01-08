def f(n):
    if n==0:
        return 1
    if n>0:
        return 2*a[1-n]+3*a[n-1]+2
    if n<0:
        return -a[-n]

a=[0]*51
for i in range(1,51):
    a[i]=f(i)
a=str(f(50))
sm=0
for i in a:
    sm+=int(i)
print(sm)