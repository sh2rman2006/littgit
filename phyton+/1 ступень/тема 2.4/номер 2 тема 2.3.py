n=int(input("-"))
for i in range(1,n+1):
    for a in range(1,n+1):
        print(i*a, end=(" "*(5-len(str(i*a)))))
    print()




