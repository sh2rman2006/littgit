a=int(input("количество-"))
n=set()
m=set()
for i in range(a):
    n.add(int(input("в список n-")))
for i in range(a):
    m.add(int(input("в список m-")))
print(len(n&m))
