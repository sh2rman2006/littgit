a=tuple(input("-").split())
el=input("-")
b=a.index(el)
c=tuple(a[:b]).__add__(a[b+1::])
print(c)
