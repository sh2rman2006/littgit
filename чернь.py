b=[int(i) for i in open('8 60 1 40.txt')]
mx=0
for i in range(len(b)):
    for k in range(i+1,len(b)):
        if (b[i]*b[k])%21==0:
            mx=max(mx,b[i]*b[k])
print(mx)
            



