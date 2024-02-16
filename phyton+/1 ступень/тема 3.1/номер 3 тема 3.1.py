n=int(input("количество-"))
a=set()
b=set()
for i in range(n):
    a.add(input("растение-"))
b.add(input("последнее растение-"))
if b&a:
    print("Вы повторяетесь")
else:
    print("все верно")


