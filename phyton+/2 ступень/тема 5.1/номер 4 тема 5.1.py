def eq():
    a=int(input("a-"))
    b=int(input("b-"))
    c=int(input("c-"))
    d=b**2-4*a*c
    if d<0:
        print("корней нет!")
    if d==1:
        print("x1=", -b/2*a)
    if d>0:
        print("x1=", (-b-d**(1/2))/2*a)
        print("x2=", (-b+d**(1/2))/2*a)

eq()