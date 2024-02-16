n=set()
m=set()
a=int(input("количество-"))
for i in range(a):
    n.add(int(input("в список n-")))
for i in range(a):
    m.add(int(input("в список m-")))
print(n^m)
