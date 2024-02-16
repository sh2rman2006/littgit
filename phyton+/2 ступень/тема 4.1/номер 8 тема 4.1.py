a=[]
for i in range(int(input("Количество-"))):
    a.append(int(input("Введите рост других учеников-")))
x=int(input(" Введите рост пети-"))
for i in range(len(a)):
    if x>a[i]:
        break
print(a)
print(i+1)






