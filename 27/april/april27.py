file=[list(map(int,i.split())) for i in open('27_A.txt')]
file.sort(reverse=1)

for i in range(len(file)):
    file[i]=sorted(file[i])
file.sort(reverse=1)


a=file[0]
count=0
for i in range(len(file)):
    if a[0]>file[i][0] and a[1]>file[i][1] and a[2]>file[i][2]:
        mn=10000
        c=sum(a)-sum(file[i])
        for k in range(i+1,len(file)):
            mn=min(mn,sum(a)-sum(file[k]))
            if c>mn:
                a=file[k]
                count+=1
            



            
            
print(count)