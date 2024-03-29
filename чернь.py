"""14233"""
for x in [k*0.25 for k in range(-10000,10000)]:
    p=17<=x<=46
    q=22<=x<=57
    a=0
    f= (not a) <=((p and q)<=a)
    if f!=1:
        print(x)
