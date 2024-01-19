<<<<<<< Updated upstream
m=0
a=18 * 7**108 - 5 * 49**76 + 343**35 - 50
def perevod(n,s):
    a=[]
    while n>0:
        a.append(str(n%s))
        n//=s
    return a[::-1]
a=perevod(a, 49)
for i in a:
    m+=a[i]
print(int(m))
=======


def f(n,s,k):
    if n%2!=0:
        k+=1
    if n==s:
        return 1
    if n>s or k>2:
        return 0
    return f(n+2,s,k)+f(n*2,s,k)
print(f(3,20,0)*f(20,68,0))
>>>>>>> Stashed changes
