a=open('27A.1.txt')
b=[int(i) for i in a]
k=b[0]
b=b[1:]
mx=-10000000
for i in range(len(b)-2*289):
    pr=b[i]*b[i+289]*b[i+2*289]
    mx=max(mx,pr)
print(mx)


