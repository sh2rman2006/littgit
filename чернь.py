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
