a=0
b = int(input("Введите число-"))
sum=0
ot=0
while b!=0:
    b = int(input("Введите число-"))
    if b>0:
        sum+=b
    elif b<0:
        ot+=b
        a += 1
print(sum,ot)




