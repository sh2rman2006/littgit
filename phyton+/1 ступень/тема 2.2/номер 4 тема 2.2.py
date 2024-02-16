a=int(input("Введите a-"))
b=int(input("Введите b-"))
if a<b:
    print(*range(a,b+1))
else:
    print(*range(a,b-1,-1))



