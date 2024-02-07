a=open('17.vala.txt')
b=[int(i) for i in a]
def s(n):
    sm=0
    for i in str(n):
        sm+=int(i)
    return sm
count=0
mx=0
for i in range(len(b)-2):
    if len(str(b[i]))==4 and len(str(b[i+1]))==4 and len(str(b[i+2]))==4:
        c=set()
        c.add(s(b[i]))
        c.add(s(b[i+1]))
        c.add(s(b[i+2]))
        sm=str(b[i]+b[i+1]+b[i+2])
        if len(c)==3 and sm==sm[::-1]:
            count+=1
            mx=max(mx,max(c))
print(count,mx)




