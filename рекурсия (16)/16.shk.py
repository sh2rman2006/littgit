from sys import *
setrecursionlimit(10000)
def g(n):
    if n<2:
        return n
    if n>=2:
        return a[n//2]+a[n%2]
a=[0]*(2**30)
for i in a :
    a[i]=g(i)
count=0
for i in range(2**30):
    if a[i]==27:
        count+=1
print(count)



