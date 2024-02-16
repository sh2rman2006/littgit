a=input("-").replace(" ","")
a=list(a)
Max=0
c=0
for i in a:
    if Max<a.count(i):
        Max=a.count(i)
        c=i
print(Max,"раз","символ-",c)





