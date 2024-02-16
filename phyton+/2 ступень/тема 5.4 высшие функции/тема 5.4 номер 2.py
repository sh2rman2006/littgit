n=int(input("n-"))
a=input("-").split()
x=filter(lambda x:len(x)>n,a)
print(*x)


