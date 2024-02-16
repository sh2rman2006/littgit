a=input("Слово-")
if len(a)%2==0:
    s=int(len(a)/2)
else:
    s=int(len(a)/2+1)
print(a[s:], a[:s])







