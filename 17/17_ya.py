a=open("17_ya.txt")
b=[int(i) for i in a]

def sumch(n):
    sm=0
    for i in str(n):
        sm+=int(i)
    return sm

mx=-100000000
count=0
for i in range(len(b)-2):
    if len(str(b[i]))==4 and len(str(b[i+1]))==4 and len(str(b[i+2]))==4:
        c=set()
        c.add(sumch(b[i]))
        c.add(sumch(b[i+1]))
        c.add(sumch(b[i+2]))
        if len(c)==3 and str(b[i]+b[i+1]+b[i+2])==str(b[i]+b[i+1]+b[i+2])[::-1]:
            count+=1
            mx=max(mx,sumch(b[i]))
            mx=max(mx,sumch(b[i+1]))
            mx=max(mx,sumch(b[i+2]))
print(count,mx)

