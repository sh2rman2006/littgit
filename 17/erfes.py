a=[123,2345,53,464,345,321,4235,3452345,45,1]
print(*filter(lambda x:x>70,a))

def od(n,s):
    ms=0
    for i in str(n):
        ms+=int(i)
    return ms
def vt(n,s):
    ms=1
    for i in str(n):
        ms*=int(i)
    return ms
def f(n,s):
    if n==s:
        return 1
    if n>s:
        return 0
    return od(n,s)+vt(n,s)
count=0
for i in range(10,101):
    if f(i,8):
        count+=1
print(count)