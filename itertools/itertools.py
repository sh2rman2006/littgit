from itertools import *
n = product("КОНФЕТА", repeat=5)
a = []
count=0
for i in n:
    a.append(list(i))

flag=True
for i in a:
    flag=True
    if i.count("Е")!=2 :
        flag=False
    if i[1]=="Ф":
        flag = False
    if flag==True:
        count+=1
print(count)




for i in range(1,101):
    for k in range(1,101):
        print(i*k,end=" "*(5-len(str(i*k))))
    print()