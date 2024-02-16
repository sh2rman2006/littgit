n=int(input("Книг в школе 1-"))
m=int(input("Книг в школе 2-"))
a=set()
b=set()
for i in range(n):
    a.add(input("книга в школе 1-"))
for o in range(m):
    b.add(input("книга в школе 2-"))
a=(a&b)
b=(b-a)
for h in a:
    print(h,"да")
for h in b:
    print(h,"нет")











