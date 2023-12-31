from itertools import *
a=product("АГДИЛНР",repeat=6)
b=[list(i) for i in a]
count=0
for i in b:
    count+=1
    if count%2==0:
        if i[0]!="Я" and i.count("Д")==3:
            print(count)

