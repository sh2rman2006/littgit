def k(n,s):
    if (n==5 or n==3) and s>=105:
        return 1
    if n==5 and s<105:
        return 0
    if n<5 and s>=105:
        return 0
    if n%2==0:
        return k(n+1,s+1) or k(n+1,s+5) or k(n+1,s*4)
    else:
        return k(n + 1, s + 1) and k(n + 1, s + 5) and k(n + 1, s * 4)
for i in range(1,105):
    if k(1,i):
        print(i)
print("/"*10)
def k(n,s):
    if n==3 and s>=105:
        return 1
    if n==3 and s<105:
        return 0
    if n<3 and s>=105:
        return 0
    if n%2==0:
        return k(n+1,s+1) or k(n+1,s+5) or k(n+1,s*4)
    else:
        return k(n + 1, s + 1) and k(n + 1, s + 5) and k(n + 1, s * 4)
for i in range(1,105):
    if k(1,i):
        print(i)