from turtle import *
"""a=Screen()
a.screensize(10000,10000)
ms=25
tracer(0)
left(90)
for i in range(4):
    forward(10*ms)
    right(90)
pu()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*ms,y*ms)
        dot(5)
done()
"""
#
a=Screen()
a.screensize(10000,10000)
ms=25
tracer(0)
left(90)
for i in range(4):
    forward(10*ms)
    right(60)
    forward(10*ms)
    right(120)
pu()
for x in range(0,100):
    for y in range(0,100):
        goto(x*ms,y*ms)
        dot(5)
done()



