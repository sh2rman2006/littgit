n=int(input("Количество-"))
a={}
for i in range(n):
    s=input(str(i+1)+" слово-")
    if s in a:
        a[s]+=1
    else:
        a[s]=1
for i,j in a.items():
    print(i, "-",j)


