
def fibb(n):
    f1=f2=1
    i=2
    while i < n:
        f1, f2 = f2, f1 + f2
        i += 1
    return f2
print(fibb(int(input("n-"))))









