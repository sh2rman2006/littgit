a=set()
b=set()
n=int(input("количество запросов-"))
for i in range(n):
    d=int(input("введите количество-"))
    for h in range(d):
        a.add(int(input("введите число-")))
    if i==0:
        b=a.copy()
    b=(a&b)
print(b)
