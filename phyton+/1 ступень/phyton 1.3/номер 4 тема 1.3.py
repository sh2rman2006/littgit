a=int(input("Введите рост 1 ученика-"))
b=int(input("Введите рост 2 ученика-"))
c=int(input("Введите рост 3 ученика-"))
a,b,c=max(a,b,c),sum([a,b,c])-(max(a,b,c)+min(a,b,c)),min(a,b,c)
print(a,b,c)


