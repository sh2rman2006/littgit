n=int(input("Записей-"))
a={}
for i in range(n):
    b=input("Страна-")
    a[b]={input("Столица-")}
s=input("Найти-")
if s in a:
    print(s,"-",a[s])
else:
    print("Вы ввели страну, о которой я не знаю")
