a=int(input("Введите количество-"))
b=0
for col in range(1, a+1):
    c=input("Введите "+str(col)+" число-")
    for i in c:
        if i=="0":
            b+=1
print(b)




