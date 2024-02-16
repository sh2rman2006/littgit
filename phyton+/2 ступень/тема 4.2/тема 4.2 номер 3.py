a=[]
n=int(input("классов-"))
m=int(input("учеников-"))
for i in range(n):
    a.append([])
    for k in range(m):
        a[i].append(int(input("класс "+str(i+1)+":"+str(k+1)+" рост ученикa-")))
r=int(input("рост от-"))
l=int(input("рост до-"))
for i in range(n):
    for k in range(m):
        if a[i][k]>=r and a[i][k]<=l:
            print("в классе",i+1,"ученик-",k+1,"-", a[i][k])

