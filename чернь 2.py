a=[]
i=14288
s=1
for d in range(2,int(i**0.5)):
    if i%d==0:
        s+=d
        s+=i//d
if i**0.5%1==0:
    s+=int(i**0.5)
a.append([i,s])
print(a)