a=[]
for i in range(1,10**6+1):
    s=1
    for d in range(2,int(i**0.5)):
        if i%d==0:
            s+=d
            s+=i//d
    if i**0.5%1==0:
        s+=int(i**0.5)
    a.append([i,s])

otv=[]
def f(n,i,l):
    for k in range(i+1,len(a)):
        if n[1]==a[k][0]:
            f(a[k],k,l+1)
        else:
            return l
    else:
        return l

for i in range(len(a)):
    s=f(a[i],i,0)
    if s>0:
        otv.append([s,a[i]])
print(otv)

