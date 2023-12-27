def f(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n>2:
        return n*(n-1)+a[n-1]-a[n-2]

a=[0]*2025
for i in range(1,2025):
    a[i]=f(i)
print(f(2024)+f(2020)-f(2018))
