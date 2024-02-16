a=float(input("Введите первое число:"))
c=input("Введите операцию (+,-,*,/,mod,pow,div):")
b=float(input("Введите второе число:"))
if c=="+":
    a+=b
    print(a)
elif c=="-":
    a-=b
    print(a)
elif c=="*":
    a*=b
    print(a)
elif c=="/" and b==0:
    print("Деление на ноль!")
elif c=="/":
    a/=b
    print(a)
elif c=="mod":
    a%=b
    print(a)
elif c=="pow":
    a**=b
    print(a)
elif c=="div":
    a//=b
    print(a)




