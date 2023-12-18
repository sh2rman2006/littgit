n=int(input("Введите число-"))
b=0
for i in range(1,n+1):
    if n%i==0:
        print(i)
        b+=1
print("Количество делителей-",b)





