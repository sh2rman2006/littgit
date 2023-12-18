a=open("17var04.txt")
b=[int(i) for i in a]
mi=10000000000000
for i in b:
    if str(i)[-3:]=="700":
        mi=min(mi,i)

md=10000000000000000
count=0
for i in range(len(b)-2):
    k=0
    if len(str(abs(b[i])))==5 :
        k+=1
    if len(str(abs(b[i+1])))==5 :
        k+=1
    if len(str(abs(b[i+2])))==5:
        k+=1
    if k<3:
        sm=b[i]+b[i+1]+b[i+2]
        if sm>=mi:
            count+=1
            md=min(md,sm)

print(count,md)



