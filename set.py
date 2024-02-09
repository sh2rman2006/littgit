a=set()
b=set()

for i in  range(1,21):
    a.add(i)
for i in range(10,31):
    b.add(i)
print(a,"a".upper(),b,"b".upper())
print(a&b,"&")
print(a|b,"|")
print(a-b,"-")
