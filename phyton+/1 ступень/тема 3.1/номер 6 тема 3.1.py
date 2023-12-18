a = set()
b = set()
n = int(input("количество в а-"))
for i in range(n):
    a.add(int(input("в а-")))
m = int(input("количество в b-"))
for i in range(m):
    b.add(int(input("в b-")))
a = (a & b)
for n in a:
    print(sorted(a))









