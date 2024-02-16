a=int(input("Введите 1 число-"))
b=int(input("Введите 2 число-"))
if a<b:
    x=a
else:
    x=b
f=True
while f:
    if (a % x) == 0 and (b % x) == 0:
        f=False
    else:
        x-=1
print(x)
