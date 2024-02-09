k=81
n=790
a=open("27_2_A.txt")
b=[int(i) for i in a]
mx=-10000000
for i in range(len(b)-2*k):
    mx=max(b[i]+b[i+k]+b[i+2*k],mx)
print(mx)