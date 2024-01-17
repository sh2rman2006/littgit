countdel=0
for i in range(10**7,2,-1):
    counti=0
    for d in range(2,int(i**0.5)):
        if i%d==0:
            counti+=2
    if i**0.5%1==0:
        counti+=1
    if counti==0:
        countdel+=1
        print(10 ** 7 - i,i )
        if countdel>4:
            break
print("????????????????")
countdel=0
for i in range(10**7,10**8):
    counti=0
    for d in range(2,int(i**0.5)):
        if i%d==0:
            counti+=2
    if i**0.5%1==0:
        counti+=1
    if counti==0:
        countdel+=1
        print(abs(10 ** 7 - i),i )
        if countdel>4:
            break
